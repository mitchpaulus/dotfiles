# Mypy

## Finding imports

[Mapping file paths to modules](https://mypy.readthedocs.io/en/latest/running_mypy.html#mapping-file-paths-to-modules)

[Namespace vs regular package](https://stackoverflow.com/questions/21819649/namespace-vs-regular-package)

Another example of why I can't stand Python sometimes.

There is a difference between a "namespace package" and a "regular package".

A namespace package allows you to have the same directory name underneath two different locations in the PATH.

Regular packages, or directories, need an `__init__.py` file in


## Config file

```
[mypy]
namespace_packages=True
```
