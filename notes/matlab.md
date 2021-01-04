# Matlab

## Throwing Exceptions

```matlab
myexception = MException('MyComponent:noSuchVariable', 'Variable %s not found', str);
throw(myexception)
```
