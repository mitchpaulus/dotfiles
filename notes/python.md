# Python

- Opening a file:
    - `with open('File path') as file:`
    - Read lines with `file.readlines()`
- String operations
    - Trim/Strip: `str_object.strip()`
    - Split: `str_object.split(split_string)`
- Truthiness
    - All values are considered "truthy" except for the following, which are "falsy":
            1. None
            2. False
            3. 0
            4. 0.0
            5. 0j
            6. Decimal(0)
            7. Fraction(0, 1)
            8. [] - an empty list
            9. {} - an empty dict
            10. () - an empty tuple
            11. '' - an empty str
            12. b'' - an empty bytes
            13. set() - an empty set
            14. an empty range, like range(0)
            15. objects for which
                1. obj.__bool__() returns False
                2. obj.__len__() returns 0
