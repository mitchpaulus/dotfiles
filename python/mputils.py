import os
from typing import List, Union, Iterable, TypeVar, Callable, Dict, Any
import re
import math

T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')

def groupby(iterable: Iterable[T1], key_selector: Callable[[T1], T2], value_selector:Callable[[T1], T3]=None) -> Dict[T2, List[T3]]:
    if value_selector is None:
        value_selector = lambda x: x

    output_dict = {}

    for item in iterable:
        key = key_selector(item)
        if key not in output_dict:
            output_dict[key] = []

        value = value_selector(item)
        output_dict[key].append(value)

    return output_dict


# From https://stackoverflow.com/a/1724723/5932184
def find_all(name: str, path: str) -> List[str]:
    """
    Find all files in path (including subdirectories) with filename name.
    """
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


def find_all_regex(regex_pattern: str, path: str) -> List[str]:
    regex = re.compile(regex_pattern)
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if regex.search(file):
                result.append(os.path.join(root, file))
    return result


def read_tsv(file_path: str, delim: str="\t", skip: int=0) -> List[List[str]]:
    """
    Read a tsv file, returning list of list of strings. The final stirng does
    not contain the new line character. Reads the file as UTF-8.
    """
    with open(file_path, encoding="utf-8") as file:
        return [line.split(delim) for line in file.read().splitlines()][skip:]


def convert_to_int_if_possible(s: str) -> Union[int, str]:
    """
    Convert the given string to an int if possible. Otherwise, return the
    original string.
    """
    return int(s) if s.isdigit() else s

def alphanum_key(s) -> List[Union[str, int]]:
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [convert_to_int_if_possible(c) for c in re.split('([0-9]+)', s)]

def str_list(l: List[Any]) -> List[str]:
    """
    Return a string representation of the given list.
    """
    return [str(x) for x in l]

# Basically taken from https://stackoverflow.com/a/2669120/5932184
def version_sort(l: Iterable[str]) -> List[str]:
    """ Sort the given iterable in the way that humans expect."""
    return sorted(l, key=alphanum_key)

def version_sort_in_place(l: List[str]):
    """ Sort the given list in the way that humans expect."""
    l.sort(key=alphanum_key)

def percentile(array: List[float], percent: float) -> float:
    """
    Returns the percentile of the list of data.
    See https://en.wikipedia.org/wiki/Percentile, Nearest-Rank method.
    :param array: List of data
    :param percent: Percentile to return (0-100)
    """
    index = math.ceil((percent / 100) * len(array))
    # Clamp index between 0 and len(array)
    index = max(1, min(index, len(array) - 1))

    return sorted(array)[index - 1]
