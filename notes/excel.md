# Excel

## Pitfalls when copying text to Excel
 - Excel will use current settings from 'Data to Columns' dialog
 - Excel will use quotes to escape your delimited string.
    - You can escape the quote character by using 3 quotes `"""`
    - This bit me on points dump from Andover where units have '"w.g.'
      as a unit.
