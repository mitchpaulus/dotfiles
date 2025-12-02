import sys
import pymupdf

if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        print("Usage: get_bookmarks.py [file.pdf]")
        print("Usage: get_bookmarks.py < [file.pdf]")
        print("Prints the bookmarks of a PDF file to stdout.")
        sys.exit(0)

    if len(sys.argv) == 1:
        doc = pymupdf.open(stream=sys.stdin.buffer.read())
    elif len(sys.argv) == 2:
        doc = pymupdf.open(sys.argv[1])
    else:
        print(f"ARGS: {len(sys.argv)}", file=sys.stderr)
        for arg in sys.argv:
            print(f"ARG: {arg}", file=sys.stderr)
        print("Usage: get_bookmarks.py [file.pdf]", file=sys.stderr)
        print("Usage: get_bookmarks.py < [file.pdf]", file=sys.stderr)
        print("Prints the bookmarks of a PDF file to stdout.", file=sys.stderr)
        sys.exit(1)

    toc = doc.get_toc()
    for item in toc:
        print(f"{item[0]}\t{item[1]}\t{item[2]}")
