#!/usr/bin/env python3

import fitz
import sys

input_file = sys.argv[1]
start_page = int(sys.argv[2])
end_page = int(sys.argv[3])
output_file = sys.argv[4]

with open(input_file) as file:
    doc = fitz.open(file)

    if start_page < 0 or end_page >= len(doc):
        print("Invalid page range.")
        sys.exit(1)

    if start_page > end_page:
        print("Start page must be less than or equal to end page.")
        sys.exit(1)

    # Create a new PDF document
    new_doc = fitz.open()

    # Add the specified pages to the new document
    for page_num in range(start_page, end_page + 1):
        new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)

    # Save the new document
    new_doc.save(output_file)
    new_doc.close()
    doc.close()
