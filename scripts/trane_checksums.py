#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf"]
# ///
"""Extract data from Trane TRACE 700 Zone/System Checksums PDF reports to JSON.

Usage:
    uv run trane_checksums.py "Zone Checksums.pdf" [-o output.json]

The TRACE checksum report is a fixed-form landscape page, one zone/system per
page.  Text extraction order is jumbled, so this parses by word coordinates:
values are right-aligned to fixed column x-positions within each section.
"""

import argparse
import json
import re
import sys

TOL = 6.0  # tolerance (pts) when matching a value's right edge to a column


def parse_num(s):
    s = s.replace(",", "")
    try:
        return float(s) if "." in s else int(s)
    except ValueError:
        return None


def slug(label):
    label = label.replace("==>", "").strip()
    label = label.replace("²", "2").replace("·", "_").replace("°", "")
    label = re.sub(r"[^A-Za-z0-9]+", "_", label).strip("_").lower()
    return label


def cluster_rows(words, tol=2.0):
    """Group words into rows by vertical position."""
    rows = []
    for w in sorted(words, key=lambda w: ((w[1] + w[3]) / 2, w[0])):
        yc = (w[1] + w[3]) / 2
        if rows and abs(yc - rows[-1][0]) <= tol:
            rows[-1][1].append(w)
            rows[-1][0] = (rows[-1][0] * (len(rows[-1][1]) - 1) + yc) / len(rows[-1][1])
        else:
            rows.append([yc, [w]])
    return [(y, sorted(ws, key=lambda w: w[0])) for y, ws in rows]


def words_in(words, x0=None, x1=None, y0=None, y1=None):
    out = []
    for w in words:
        xc = (w[0] + w[2]) / 2
        yc = (w[1] + w[3]) / 2
        if x0 is not None and xc < x0:
            continue
        if x1 is not None and xc > x1:
            continue
        if y0 is not None and yc < y0:
            continue
        if y1 is not None and yc > y1:
            continue
        out.append(w)
    return out


def find_phrase(words, phrase):
    """Return bbox (x0,y0,x1,y1) of first occurrence of a word sequence."""
    seq = phrase.split()
    rows = cluster_rows(words)
    for _, ws in rows:
        texts = [w[4] for w in ws]
        for i in range(len(texts) - len(seq) + 1):
            if texts[i : i + len(seq)] == seq:
                grp = ws[i : i + len(seq)]
                return (
                    min(w[0] for w in grp),
                    min(w[1] for w in grp),
                    max(w[2] for w in grp),
                    max(w[3] for w in grp),
                )
    return None


def parse_columnar(words, label_x, col_edges, y0, y1):
    """Parse rows: label words in label_x window, values matched to column
    right-edges.  Returns list of {name, <col>: value} dicts."""
    out = []
    for _, ws in cluster_rows(words_in(words, y0=y0, y1=y1)):
        label_words, values = [], {}
        for w in ws:
            if label_x[0] <= w[0] < label_x[1] and parse_num(w[4]) is None:
                label_words.append(w[4])
                continue
            n = parse_num(w[4])
            if n is None:
                continue
            # match right edge to nearest column
            best = min(col_edges.items(), key=lambda c: abs(w[2] - c[1]))
            if abs(w[2] - best[1]) <= TOL:
                values[best[0]] = n
        if label_words and values:
            row = {"name": " ".join(label_words).replace("==>", "").strip()}
            row.update(values)
            out.append(row)
    return out


def parse_two_col(words, label_x, cool_edge, heat_edge, y0, y1):
    """Parse sidebar sections with Cooling / Heating value columns."""
    out = {}
    for _, ws in cluster_rows(words_in(words, y0=y0, y1=y1)):
        label_words, cooling, heating = [], None, None
        for w in ws:
            n = parse_num(w[4])
            if label_x[0] <= w[0] < label_x[1] and n is None:
                if w[4] not in ("Cooling", "Heating"):
                    label_words.append(w[4])
                continue
            if n is None:
                continue
            if abs(w[2] - cool_edge) <= TOL or w[2] < (cool_edge + heat_edge) / 2:
                cooling = n
            elif abs(w[2] - heat_edge) <= TOL:
                heating = n
        if label_words and (cooling is not None or heating is not None):
            out[slug(" ".join(label_words))] = {"cooling": cooling, "heating": heating}
    return out


def parse_peak_header(words, y_mohr):
    """Parse the three 'Mo/Hr:' peak-time entries and OADB line."""
    words = words_in(words, x1=608)  # exclude the TEMPERATURES sidebar
    rows = cluster_rows(words)
    mohr_row = min(rows, key=lambda r: abs(r[0] - y_mohr))
    ws = mohr_row[1]
    anchors = [w for w in ws if w[4] == "Mo/Hr:"]
    peaks = []
    for i, a in enumerate(anchors):
        x_end = anchors[i + 1][0] if i + 1 < len(anchors) else 800
        toks = [w[4] for w in ws if a[2] < w[0] < x_end]
        text = " ".join(toks)
        m = re.match(r"(\d+)\s*/\s*(\d+)", text)
        if m:
            peaks.append({"month": int(m.group(1)), "hour": int(m.group(2))})
        else:
            peaks.append(text if text else None)
    return peaks


def parse_oadb_row(words, y):
    """Parse the OADB/WB/HR header line -> (cooling {db,wb,hr}, space db, heating db)."""
    rows = cluster_rows(words_in(words, x1=608))  # exclude the sidebar
    row = min(rows, key=lambda r: abs(r[0] - y))
    ws = row[1]
    result: dict = {"cooling": None, "space": None, "heating": None}
    nums = []
    anchor = None
    entries = []  # (anchor_label, [nums])
    for w in ws:
        if w[4].endswith(":"):
            if anchor:
                entries.append((anchor, nums))
            anchor, nums = w[4], []
        elif anchor:
            n = parse_num(w[4])
            if n is not None:
                nums.append(n)
    if anchor:
        entries.append((anchor, nums))
    slots = ["cooling", "space", "heating"]
    i = 0
    for label, ns in entries:
        if label == "OADB/WB/HR:" and len(ns) == 3:
            result[slots[i]] = {"db": ns[0], "wb": ns[1], "hr": ns[2]}
            i += 1
        elif label == "OADB:" and ns:
            result[slots[i]] = {"db": ns[0]}
            i += 1
        elif label in ("OADB/WB/HR:", "OADB:"):
            i += 1
    return result


def parse_page(page):
    words = page.get_text("words")
    text = page.get_text()

    # ---- report type: System / Zone / Room Checksums ----
    report_type = None
    for t in ("System", "Zone", "Room"):
        if f"{t} Checksums" in text:
            report_type = t
            break

    # ---- anchors ----
    b_temps = find_phrase(words, "TEMPERATURES")
    b_air = find_phrase(words, "AIRFLOWS")
    b_eng = find_phrase(words, "ENGINEERING CKS")
    b_areas = find_phrase(words, "AREAS")
    b_ccp = find_phrase(words, "COOLING COIL PEAK")
    b_footer = find_phrase(words, "Project Name:")
    y_bottom = b_areas[1] if b_areas else 450
    y_footer = b_footer[1] if b_footer else 560

    # ---- zone name: words above the peak-table headers, left of center ----
    y_hdr = b_ccp[1] if b_ccp else 84
    zone_words = [w for w in words_in(words, y0=60, y1=y_hdr - 2) if w[0] < 320]
    zone = " ".join(w[4] for w in sorted(zone_words, key=lambda w: w[0])) or None

    # ---- peak times & outdoor-air conditions ----
    peaks = parse_peak_header(words, y_hdr + 14)
    oadb = parse_oadb_row(words, y_hdr + 23)

    # ---- main load tables (fixed column right-edges) ----
    y_tbl0 = y_hdr + 70  # below the column-header block
    y_tbl1 = y_bottom - 8
    cool_cols = {
        "space_sens_lat_btuh": 159.3,
        "plenum_sens_lat_btuh": 207.3,
        "net_total_btuh": 256.0,
        "percent_of_total": 290.4,
    }
    space_cols = {
        "space_sensible_btuh": 344.2,
        "percent_of_total": 378.6,
    }
    heat_cols = {
        "space_peak_space_sens_btuh": 511.9,
        "coil_peak_tot_sens_btuh": 569.9,
        "percent_of_total": 602.1,
    }
    left_words = words_in(words, x0=45, x1=382, y0=y_tbl0, y1=y_tbl1)
    cooling_rows = parse_columnar(left_words, (45, 132), cool_cols, y_tbl0, y_tbl1)
    space_rows = parse_columnar(left_words, (45, 132), space_cols, y_tbl0, y_tbl1)
    right_words = words_in(words, x0=383, x1=606, y0=y_tbl0, y1=y_tbl1)
    heating_rows = parse_columnar(right_words, (383, 465), heat_cols, y_tbl0, y_tbl1)

    # ---- sidebar: temperatures / airflows / engineering checks ----
    side = words_in(words, x0=608, x1=752)
    temps = parse_two_col(side, (608, 662), 701.4, 738.8, b_temps[3], b_air[1]) if b_temps and b_air else {}
    air = parse_two_col(side, (608, 662), 706.1, 743.4, b_air[3], b_eng[1]) if b_air and b_eng else {}
    eng = parse_two_col(side, (608, 662), 701.4, 738.8, b_eng[3], y_bottom) if b_eng else {}

    # ---- bottom: coil selections & areas ----
    y_sel0 = y_bottom + 28  # below the units header rows
    ccs_cols = {
        "ton": 121.3, "total_capacity_mbh": 159.2, "sens_cap_mbh": 204.4,
        "coil_airflow_cfm": 254.7, "enter_db_f": 278.7, "enter_wb_f": 302.4,
        "enter_hr_grlb": 331.6, "leave_db_f": 371.9, "leave_wb_f": 390.5,
        "leave_hr_grlb": 417.6,
    }
    area_cols = {"gross_total_ft2": 500.7, "glass_ft2": 530.7, "glass_percent": 557.0}
    hcs_cols = {
        "capacity_mbh": 652.1, "coil_airflow_cfm": 700.2,
        "ent_f": 720.2, "lvg_f": 746.5,
    }
    ccs = parse_columnar(words_in(words, x0=45, x1=420), (45, 106), ccs_cols, y_sel0, y_footer)
    areas = parse_columnar(words_in(words, x0=428, x1=560), (428, 470), area_cols, y_sel0, y_footer)
    hcs = parse_columnar(words_in(words, x0=564, x1=752), (564, 610), hcs_cols, y_sel0, y_footer)

    def keyed(rows):
        out = {}
        for r in rows:
            name = r.pop("name")
            key = slug(name)
            n = 2
            while key in out:  # e.g. repeated "Sub Total" rows
                key = f"{slug(name)}_{n}"
                n += 1
            out[key] = r
        return out

    # ---- derived: lights & misc load density (W/ft2) ----
    areas_keyed = keyed(areas)
    floor_ft2 = areas_keyed.get("floor", {}).get("gross_total_ft2")
    cooling_keyed = keyed(cooling_rows)
    if floor_ft2:
        for name in ("lights", "misc"):
            row = cooling_keyed.get(name)
            if row and row.get("net_total_btuh") is not None:
                row["w_per_ft2"] = round(row["net_total_btuh"] / 3.412 / floor_ft2, 3)

    # ---- footer metadata (by coordinates; raw text order is jumbled) ----
    calc = re.search(r"calculated at (.+?) on (\d{2}/\d{2}/\d{4})", text)
    pageinfo = re.search(r"Page (\d+) of (\d+)", text)
    project = dataset = alternative = None
    for _, ws in cluster_rows(words_in(words, y0=y_footer - 2)):
        line = " ".join(w[4] for w in ws)
        m = re.match(r"Project Name:\s*(.*?)\s*(?:TRACE®.*)?$", line)
        if m and m.group(1):
            project = m.group(1)
        m = re.match(r"Dataset Name:\s*(.*?)\s*(?:(Alternative.*?)\s+System Checksums.*)?$", line)
        if m:
            dataset = m.group(1) or None
            alternative = m.group(2)

    return {
        "zone": zone,
        "report_type": report_type,
        "cooling_coil_peak": {
            "peaked_at": peaks[0] if len(peaks) > 0 else None,
            "outside_air": oadb["cooling"],
            "loads": cooling_keyed,
        },
        "clg_space_peak": {
            "peaked_at": peaks[1] if len(peaks) > 1 else None,
            "outside_air": oadb["space"],
            "loads": keyed(space_rows),
        },
        "heating_coil_peak": {
            "peaked_at": peaks[2] if len(peaks) > 2 else None,
            "outside_air": oadb["heating"],
            "loads": keyed(heating_rows),
        },
        "temperatures": temps,
        "airflows": air,
        "engineering_checks": eng,
        "areas": areas_keyed,
        "cooling_coil_selection": keyed(ccs),
        "heating_coil_selection": keyed(hcs),
        "footer": {
            "calculated": f"{calc.group(1)} on {calc.group(2)}" if calc else None,
            "project_name": project,
            "dataset_name": dataset,
            "alternative": alternative,
            "page": int(pageinfo.group(1)) if pageinfo else None,
        },
    }


AIR_BTUH_PER_CFM_F = 1.085  # sensible air factor, Btu/h per CFM·°F
INDOOR_DB_F = 75.0  # assumed indoor drybulb for infiltration back-calc

SUMMARY_COLS = [
    "unit", "type", "floor_area_ft2", "wall_area_ft2", "roof_area_ft2",
    "lighting_w_ft2", "plug_w_ft2", "no_people", "people_btuh_per_person",
    "design_cfm", "clg_infil_cfm", "clg_infil_btuh",
    "htg_infil_cfm", "htg_infil_btuh", "clg_cfm_ft2", "htg_cfm_ft2",
]


def dig(d, *keys):
    for k in keys:
        d = d.get(k) if isinstance(d, dict) else None
    return d


def summarize_zone(z):
    floor = dig(z, "areas", "floor", "gross_total_ft2")

    people = dig(z, "engineering_checks", "no_people", "cooling")
    people_btuh = dig(z, "cooling_coil_peak", "loads", "people", "net_total_btuh")
    per_person = round(people_btuh / people, 1) if people and people_btuh is not None else None

    def airflow(mode):
        for row in ("main_fan", "diffuser", "terminal"):
            v = dig(z, "airflows", row, mode)
            if v is not None:
                return v
        return None

    def infil(load, oa_db, mode):
        """Back-calc infiltration CFM from sensible load and OA-indoor dT."""
        if load is None or oa_db is None:
            return None
        dt = (oa_db - INDOOR_DB_F) if mode == "cooling" else (INDOOR_DB_F - oa_db)
        if dt <= 0:
            return None
        return round(abs(load) / (AIR_BTUH_PER_CFM_F * dt), 1)

    clg_infil_btuh = dig(z, "cooling_coil_peak", "loads", "infiltration", "net_total_btuh")
    htg_infil_btuh = dig(z, "heating_coil_peak", "loads", "infiltration", "coil_peak_tot_sens_btuh")
    if htg_infil_btuh is None:
        htg_infil_btuh = dig(z, "heating_coil_peak", "loads", "infiltration", "space_peak_space_sens_btuh")
    clg_oa = dig(z, "cooling_coil_peak", "outside_air", "db")
    htg_oa = dig(z, "heating_coil_peak", "outside_air", "db")

    def cfm_ft2(mode):
        v = dig(z, "engineering_checks", "cfm_ft2", mode)
        if v is not None:
            return v
        cfm = airflow(mode)
        return round(cfm / floor, 3) if cfm is not None and floor else None

    return {
        "unit": z.get("zone"),
        "type": z.get("report_type"),
        "floor_area_ft2": floor,
        "wall_area_ft2": dig(z, "areas", "wall", "gross_total_ft2"),
        "roof_area_ft2": dig(z, "areas", "roof", "gross_total_ft2"),
        "lighting_w_ft2": dig(z, "cooling_coil_peak", "loads", "lights", "w_per_ft2"),
        "plug_w_ft2": dig(z, "cooling_coil_peak", "loads", "misc", "w_per_ft2"),
        "no_people": people,
        "people_btuh_per_person": per_person,
        "design_cfm": airflow("cooling"),
        "clg_infil_cfm": infil(clg_infil_btuh, clg_oa, "cooling"),
        "clg_infil_btuh": clg_infil_btuh,
        "htg_infil_cfm": infil(htg_infil_btuh, htg_oa, "heating"),
        "htg_infil_btuh": htg_infil_btuh,
        "clg_cfm_ft2": cfm_ft2("cooling"),
        "htg_cfm_ft2": cfm_ft2("heating"),
    }


def summary_tsv(zones):
    lines = ["\t".join(SUMMARY_COLS)]
    for z in zones:
        row = summarize_zone(z)
        lines.append("\t".join("" if row[c] is None else str(row[c]) for c in SUMMARY_COLS))
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Extract TRACE 700 zone checksum reports to JSON")
    ap.add_argument("pdf", help="path to the checksums PDF")
    ap.add_argument("-o", "--output", help="output file (default: stdout)")
    ap.add_argument("--summary", action="store_true",
                    help="output a one-row-per-unit TSV summary instead of JSON")
    args = ap.parse_args()

    import fitz

    doc = fitz.open(args.pdf)
    zones = [parse_page(p) for p in doc]
    result = {"source": args.pdf, "zones": zones}

    out = summary_tsv(zones) if args.summary else json.dumps(result, indent=2)
    if args.output:
        with open(args.output, "w") as f:
            f.write(out)
        print(f"Wrote {len(zones)} zones to {args.output}", file=sys.stderr)
    else:
        print(out)


if __name__ == "__main__":
    main()
