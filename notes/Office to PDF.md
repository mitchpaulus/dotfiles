`https://github.com/cognidox/OfficeToPDF`

```
C:\Users\test> officetopdf.exe somefile.docx somefile.pdf
```

Switches:

The following optional switches can be used:

| Switch | Description |
| ------ | ----------- |
| /bookmarks                 | create bookmarks in the PDF when they are supported by the Office application |
| /readonly                  | attempts to open the source document in read-only mode |
| /print                     | create high-quality PDFs optimised for print |
| /hidden                    | attempts to minimise the Office application when converting |
| /template _template_       | use a .dot, .dotx or .dotm template when converting with Word |
| /markup                    | show document markup when creating PDFs with Word |
| /pdfa                      | produce ISO 19005-1 (PDF/A) compliant PDFs |
| /noquit                    | do not exit running Office applications |
| /excludeprops              | do not include properties in generated PDF |
| /excludetags               | do not include tags in generated PDF |
| /password _password_       | provide a read password to open the file with |
| /writepassword _password_  | provide a read/write password to open the file with |
| /merge                     | when using a template, create a new file from the template and merge the text from the document to convert into the new file |
| /excel_show_formulas       | show formulas in Excel |
| /excel_show_headings       | shows column and row headings |
| /excel_max_rows _rows_     | allow a limit on the number of rows to convert |
| /excel_active_sheet        | only convert the currently active worksheet in a spreadsheet |
| /excel_worksheet _num_     |  only convert worksheet _num_ in the workbook. First sheet is 1 |
| /excel_auto_macros         | run Auto_Open macros in Excel files before conversion |
| /excel_no_link_update      | do not update links when opening Excel files |
| /excel_no_recalculate      | skip automatic re-calculation of formulas in the workbook |
| /word_header_dist _pts_    | the distance (in points) from the header to the top of the page |
| /word_footer_dist _pts_    | the distance (in points) from the footer to the bottom of the page |
| /word_field_quick_update   | perform a fast update of fields in Word before conversion |
| /word_fix_table_columns    | update table column widths to match table heading column widths |
| /word_keep_history         | do not clear Word's recent files list |
| /word_max_pages _pages_    | do not attempt conversion of a Word document if it has more than this number of _pages_ |
| /word_no_field_update      | do not update fields when creating the PDF |
| /word_ref_fonts            | when fonts are not available, a reference to the font is used in the generated PDF rather than a bitmapped version. The default is for a bitmap of the text to be used |
| /word_show_comments        | show comments when /markup is used |
| /word_show_revs_comments   | show revisions and comments when /markup is used |
| /word_show_format_changes  | show format changes when /markup is used |
| /word_show_ink_annot       | show ink annotations when /markup is used |
| /word_show_ins_del         | show all markup when /markup is used |
| /word_show_all_markup      | show all markup content when /markup is used |
| /word_markup_balloon       | show balloon style markup messages rather than inline ones |
| /fallback_printer <name>   | print the document to postscript printer <name> for conversion when the main conversion routine fails. Requires Ghostscript to be installed |
| /printer <name>            | print the document to postscript printer <name> for conversion. Requires Ghostscript to be installed |
| /pdf_clean_meta _type_     | allows for some meta-data to be removed from the generated PDF<br>_type_ can be:<ul><li>basic - removes author, keywords, creator and subject</li><li>full - removes all that basic removes and also the title</li></ul> |
| /pdf_layout _layout_       | controls how the pages layout in Acrobat Reader<br>_layout_ can be one of the following values:<ul><li>onecol - show pages as a single scrolling column</li><li>single - show pages one at a time</li><li>twocolleft - show pages in two columns, with odd-numbered pages on the left</li><li>twocolright - show pages in two columns, with odd-numbered pages on the right</li><li>twopageleft - show pages two at a time, with odd-numbered pages on the left</li><li>twopageright - show pages two at a time, with odd-numbered pages on the right</li></ul> |
| /pdf_page_mode _mode_      | controls how the PDF will open with Acrobat Reader<br>_mode_ can be one of the following values:<ul><li>full - the PDF will open in fullscreen mode</li><li>bookmarks - the PDF will open with the bookmarks visible</li><li>thumbs - the PDF will open with the thumbnail view visible</li><li>none - the PDF will open without the navigation bar visible</li></ul> |
| /pdf_append                | append the generated PDF to the end of the PDF destination |
| /pdf_prepend               | prepend the generated PDF to the start of the PDF destination |
| /pdf_owner_pass _pass_     | set the owner password on the PDF. Needed to make modifications to the PDF |
| /pdf_user_pass _pass_      | set the user password on the PDF. Needed to open the PDF |
| /pdf_restrict_accessibility_extraction | Prevent all content extraction without the owner password |
| /pdf_restrict_annotation   | prevent annotations on the PDF without the owner password |
| /pdf_restrict_assembly     |  prevent rotation, removal or insertion of pages without the owner password |
| /pdf_restrict_extraction   |  prevent content extraction without the owner password |
| /pdf_restrict_forms        | prevent form entry without the owner password |
| /pdf_restrict_full_quality | prevent full quality printing without the owner password |
| /pdf_restrict_modify       | prevent modification without the owner password |
| /pdf_restrict_print        | prevent printing without the owner password |
| /verbose                   | print out messages as it runs |
| /version                   | print out the version of OfficeToPDF and exit |
| /working_dir _path_        | a path to copy the input file into temporarily when running the conversion |
