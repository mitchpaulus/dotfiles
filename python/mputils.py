import os
from typing import List, Union, Iterable
import re

def groupby(iterable: Iterable, key_selector, value_selector=None):
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
def find_all(name: str, path: str):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


def find_all_regex(regex_pattern: str, path: str):
    regex = re.compile(regex_pattern)
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if regex.search(file):
                result.append(os.path.join(root, file))
    return result


def read_tsv(file_path: str) -> List[List[str]]:
    with open(file_path, encoding="utf-8") as file:
        return [line.split('\t') for line in file.read().splitlines()]
