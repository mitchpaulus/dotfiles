<https://stackoverflow.com/a/14799490/5932184>
```python
def decorator(func):
   return func

@decorator
def some_func():
    pass

# Same as:
def decorator(func):
    return func

def some_func():
    pass

some_func = decorator(some_func)
```
