#!/usr/bin/env python3

# import fitz  # Import the PyMuPDF library
import pymupdf
import sys
import os
import pathlib

def merge_pdfs_with_bookmarks(pdf_entries: list[tuple[str, str | None]], output_path, filename_bookmark_mode, title=None):
    """pdf_entries is a list of (file path, optional first level bookmark) tuples."""
    merged_document = pymupdf.open()  # Create a new empty PDF document

    page_offset = 0  # Keep track of the number of pages to adjust bookmark page numbers
    bookmarks = []  # List to hold all bookmarks

    # Loop through all provided PDF files
    for pdf_file_name, first_level_bookmark in pdf_entries:
        try:
            with pymupdf.open(pdf_file_name) as doc:

                if first_level_bookmark is None and filename_bookmark_mode:
                    # Retrieve the current document's filename
                    filename = pathlib.Path(pdf_file_name).stem
                    # Add the filename as a bookmark, minus the extension
                    page = 1 + page_offset
                    bkmk = [1, filename, page]
                    print(bkmk, file=sys.stderr)
                    bookmarks.append(bkmk)
                else:
                    # Retrieve the current document's bookmarks (if any)
                    current_bookmarks = doc.get_toc(simple=True)
                    # [level, title, 1-based page, {optional dict}]

                    if first_level_bookmark is not None:
                        # Move the level for each bookmark down one
                        for bkmk in current_bookmarks:
                            bkmk[0] += 1
                        bookmarks.append([1, first_level_bookmark, page_offset + 1])

                    # Adjust the current document's bookmark page numbers and add to the main list
                    for bkmk in current_bookmarks:
                        # Increment the page number by the current offset
                        bkmk[2] += page_offset
                        #  if "page" not in bkmk[3]:
                            #  message = f"Bookmark '{bkmk[1]}' in '{pdf_file_name}' does not have a page number in optional dict. Found {bkmk[3]}"
                            #  raise ValueError(message)

                        #  # This page is 0-based, so thus the -1
                        #  bkmk[3]["page"] = int(bkmk[3]["page"]) + page_offset - 1
                        bookmarks.append(bkmk)

                # Update the page offset
                page_offset += doc.page_count

                # Append the document
                merged_document.insert_pdf(doc, annots=True)
        except Exception as e:
            print(f"Error processing '{pdf_file_name}': {e}", file=sys.stderr)
            raise e
            # sys.exit(1)

    if title is not None:
        # Single top level bookmark, with everything else shifted down a level
        for bkmk in bookmarks:
            bkmk[0] += 1
        bookmarks.insert(0, [1, title, 1])

    # Assert that there are no bookmarks with page < 1
    bad_bkmks = [bkmk for bkmk in bookmarks if bkmk[2] < 1]
    if len(bad_bkmks) > 0:
        print(f"Error: Found bookmarks with page < 1: {bad_bkmks}", file=sys.stderr)
        sys.exit(1)

    num_inserted = merged_document.set_toc(bookmarks)
    print(f"Inserted {num_inserted} bookmarks", file=sys.stderr)
    # Save the merged document
    merged_document.save(output_path)

    print("New bookmarks:", file=sys.stderr)
    for bkmk in merged_document.get_toc(simple=False):
        print(bkmk, file=sys.stderr)

    merged_document.close()


help_message = """Usage: pdfmerge.py [--filename] [--title <title>] [--from-file <file>] <output file> [input files...]

This script uses PyMuPDF to merge PDFs.

Input files on the command line can be given as 'path:bookmark' to add a first level
bookmark for that file, with the file's existing bookmarks shifted down a level.

Options:
  --filename          Add a bookmark with the filename (minus extension) as the text for
                      each file that doesn't have a specific bookmark.
  --title <title>     Add a single top level bookmark, shifting all other bookmarks down a level.
  --from-file <file>  Read input files from a TSV file. First column is the file path,
                      optional second column is a first level bookmark for that file.
                      Use '-' as the file to read the list from stdin (only once).
                      Can be given multiple times. Entries are added after command line inputs.

First level bookmark precedence for each file: specific bookmark, then --filename,
otherwise the file's existing bookmarks are kept at the top level.

Example:
  printf 'a.pdf\\tSection A\\nb.pdf\\n' | pdfmerge2 --filename --from-file - out.pdf
"""

def parse_input_file_list(lines, source) -> list[tuple[str, str | None]]:
    entries = []
    for line_num, line in enumerate(lines, start=1):
        line = line.rstrip("\r\n")
        if line.strip() == "":
            continue
        fields = line.split("\t")
        path = fields[0].strip()
        if path == "":
            print(f"Error: empty file path on line {line_num} of '{source}'", file=sys.stderr)
            sys.exit(1)
        bookmark = None
        if len(fields) > 1 and fields[1].strip() != "":
            bookmark = fields[1].strip()
        entries.append((path, bookmark))
    return entries

def read_input_files_from_file(path):
    if path == "-":
        return parse_input_file_list(sys.stdin, "<stdin>")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return parse_input_file_list(f, path)
    except Exception as e:
        print(f"Error reading input file list '{path}': {e}", file=sys.stderr)
        sys.exit(1)

def parse_input_arg(arg) -> tuple[str, str | None]:
    # Split on ':'. First part should be filename, second part should be an optional new first level bookmark.
    parts = arg.split(':', 1)
    if len(parts) > 1:
        return (parts[0], parts[1])
    return (parts[0], None)


if __name__ == "__main__":
    index = 1

    filename_bookmark_mode = False
    title = None
    input_file_lists = []

    while index < len(sys.argv):
        if sys.argv[index] == "-h" or sys.argv[index] == "--help":
            print(help_message, end="")
            sys.exit(1)
        elif sys.argv[index] == "--filename":
            filename_bookmark_mode = True
            index += 1
        elif sys.argv[index] == "--title":
            if index + 1 >= len(sys.argv):
                print("--title requires a title", file=sys.stderr)
                sys.exit(1)
            title = sys.argv[index + 1]
            index += 2
        elif sys.argv[index] == "--from-file":
            if index + 1 >= len(sys.argv):
                print("--from-file requires a path", file=sys.stderr)
                sys.exit(1)
            input_file_lists.append(sys.argv[index + 1])
            index += 2
        else:
            break

    if len(sys.argv) - index < 1:
        print(help_message)
        sys.exit(1)

    if input_file_lists.count("-") > 1:
        print("stdin ('-') can only be given once to --from-file", file=sys.stderr)
        sys.exit(1)

    output_file = sys.argv[index]
    input_entries = [parse_input_arg(arg) for arg in sys.argv[index + 1:]]
    for input_file_list in input_file_lists:
        input_entries.extend(read_input_files_from_file(input_file_list))

    if len(input_entries) == 0:
        print("At least one input file is required", file=sys.stderr)
        sys.exit(1)

    if output_file.strip() == "":
        print("Output file cannot be empty", file=sys.stderr)
        sys.exit(1)

    # Merge the PDFs
    merge_pdfs_with_bookmarks(input_entries, output_file, filename_bookmark_mode, title)
