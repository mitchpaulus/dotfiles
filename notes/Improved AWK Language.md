# Improved AWK design

I love awk. But it certainly has its flaws.
I want to create a new version for myself that is better for the types of engineering that I do.

## Requirements

- Numbers with units need to be first class. Operations need to be strict with respect to units.
- Numbers should be able to handle uncertainty parameters.
- DateTimes should be first class.
- First class functions
- Easy number formatting.
- Static type checking, add typing for columns
- String Interpolation
- HEREDOC string entry

- Built-in String splitting operators

- Field array slicing syntax
  - Something like `$2:4 ~ /something/`, where this basically checks whether *all* columns 2 through 4 match the regex.

- string operations
  - strip, stripleft, stripright


## Other language considerations

[Comments](https://www.reddit.com/r/ProgrammingLanguages/comments/w6ntc8/favorite_comment_syntax_in_programming_languages/)

Like the concept of variable length delimiters.
