#!/usr/bin/env python3

# import fitz  # Import the PyMuPDF library
import pymupdf
import sys
import os
import pathlib

def merge_pdfs_with_bookmarks(pdf_paths: list[str], output_path, filename_bookmark_mode):
    merged_document = pymupdf.open()  # Create a new empty PDF document

    page_offset = 0  # Keep track of the number of pages to adjust bookmark page numbers
    bookmarks = []  # List to hold all bookmarks

    # Loop through all provided PDF files
    for pdf_path in pdf_paths:
        # Split on ':'. First part should be filename, second part should be an optional new first level bookmark number.
        pdf_path_parts = pdf_path.split(':', 1)
        
        pdf_file_name = pdf_path_parts[0]
        first_level_bookmark = None
        if len(pdf_path_parts) > 1:
            first_level_bookmark = pdf_path_parts[1]

        try:
            with pymupdf.open(pdf_file_name) as doc:

                if filename_bookmark_mode:
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


help_message = "Usage: pdfmerge.py [--filename] <output file> <input files...>\n\nThis script uses PyMuPDF to merge PDFs. --filename can be used to add a bookmark with the filename as the text.\n"

if __name__ == "__main__":
    index = 1

    filename_bookmark_mode = False

    while index < len(sys.argv):
        if sys.argv[index] == "-h" or sys.argv[index] == "--help":
            print(help_message, end="")
            sys.exit(1)
        elif sys.argv[index] == "--filename":
            filename_bookmark_mode = True
            index += 1
        else:
            break

    if len(sys.argv) - index < 2:
        print(help_message)
        sys.exit(1)

    output_file = sys.argv[index]
    input_files = sys.argv[index + 1:]

    if output_file.strip() == "":
        print("Output file cannot be empty", file=sys.stderr)
        sys.exit(1)

    # Merge the PDFs
    merge_pdfs_with_bookmarks(input_files, output_file, filename_bookmark_mode)
