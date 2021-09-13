import os

def groupby(iterable, key_selector, value_selector=None):
    if value_selector is None:
        value_selector = lambda x: x

    output_dict = {}

    for item in iterable:
        key = key_selector(item)
        if key not in output_dict:
            output_dict[key] = []

        value = value_selector(item)
        output_dict[key].append(value)


# From https://stackoverflow.com/a/1724723/5932184
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result
