```
xargs -d '\n' command  # Use newline as delimiter
command | tr '\n' '\0' | xargs -0 command  # Use null byte as delimiter
```
