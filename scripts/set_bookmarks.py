#!/usr/bin/env python3

# USAGE
# Pass in lines of tab separated values to stdin.
# Lines are [level, title, page] where level is 1 based and page is 1 based.
# printf '1\tName\t2\n' | set_bookmarks pdf_file.pdf
import sys
import fitz

# https://pymupdf.readthedocs.io/en/latest/document.html#Document.set_toc
def set_bookmarks(pdf_file, add = False, output_file = None):

    if add:
        doc = fitz.open(pdf_file)
        bookmarks = doc.get_toc()
        doc.close()
    else:
        bookmarks = []

    prev_level = 1

    line_num = 1
    for line in sys.stdin:
        level_one_based, title, page_one_based = line.strip().split('\t')

        try:
            level_one_based = int(level_one_based)
        except ValueError:
            raise ValueError(f'Invalid level: {level_one_based}')

        try:
            page_one_based = int(page_one_based)
        except ValueError:
            raise ValueError(f'Invalid page: {page_one_based}')

        if level_one_based < 1:
            raise ValueError(f'Invalid level on line {line_num}: {level_one_based}')

        if page_one_based < 1:
            raise ValueError(f'Invalid page on line {line_num}: {page_one_based}')

        if level_one_based > prev_level + 1:
            raise ValueError(f'Invalid level on line {line_num}: {level_one_based}, previous level: {prev_level}')

        bookmarks.append([level_one_based, title, page_one_based])
        prev_level = level_one_based
        line_num += 1


    if len(bookmarks) == 0:
        print("No bookmarks found.", file=sys.stderr)

    doc = fitz.open(pdf_file)
    print(f"Setting {len(bookmarks)} bookmarks in {pdf_file}", file=sys.stderr)
    doc.set_toc(bookmarks)
    if output_file:
        doc.save(output_file, garbage=4, deflate=True)
    else:
        doc.saveIncr()
        doc.close()

if __name__ == '__main__':
    output_file = None
    pdf_file = None

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        i += 1

        if arg in ['-h', '--help']:
            print(f'Usage: {sys.argv[0]} pdf_file.pdf < INPUT_DATA')
            print('Pass in lines of tab separated values to stdin.')
            print('Lines are [level, title, page] where level is 1 based and page is 1 based.')
            print('Update the bookmarks in the PDF file in-place with the given data.')
            sys.exit(0)
        elif arg in ['-o']:
            if i >= len(sys.argv):
                print('Error: -o requires an output file argument')
                sys.exit(1)
            output_file = sys.argv[i]
            i += 1
        else:
            if output_file is not None:
                print(f'Error: unexpected argument {arg}')
                sys.exit(1)
            pdf_file = arg


    #  if len(sys.argv) != 2 or sys.argv[1] in ['-h', '--help']:
        #  print(f'Usage: {sys.argv[0]} pdf_file.pdf < INPUT_DATA')
        #  print('Pass in lines of tab separated values to stdin.')
        #  print('Lines are [level, title, page] where level is 1 based and page is 1 based.')
        #  sys.exit(0)

    if pdf_file is None:
        print('Error: pdf_file argument is required')
        sys.exit(1)

    #  pdf_file = sys.argv[1]
    set_bookmarks(pdf_file, False, output_file)
