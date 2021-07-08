# Python Function Arguments

[Official documentation](https://docs.python.org/dev/tutorial/controlflow.html#more-on-defining-functions)

```python
# * indicates the end of positional arguments
def function(pos1, pos2, *, must_be_named, another_must_be_named)
  pass
function(1, 2, must_be_named=1, another_must_be_named=2)


# Can allow for arbitrary named arguments using **
def function(pos1, pos2, **kwargs)
  type(kwargs) == dict
  kwargs['my_key'] = value
  pass

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch


# Arbitrary length parameter list
def function(pos1, *args)
  type(args) == tuple
```
