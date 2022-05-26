import os
import datetime
from typing import List, Union, Iterable, TypeVar, Callable, Dict, Any, cast
import re
import math
import sys

T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')

def groupby(iterable: Iterable[T1], key_selector: Callable[[T1], T2], value_selector:Union[Callable[[T1], T3], None]=None) -> Dict[T2, List[T3]]:
    # This is straight boilerplate to deal with mypy
    def identity(x: T1) -> T3:
        y = cast(T3, x)
        return y

    chosen_value_selector: Callable[[T1], T3] = value_selector or identity

    output_dict: Dict[T2, List[T3]] = {}

    for item in iterable:
        key = key_selector(item)
        if key not in output_dict:
            output_dict[key] = []

        value = chosen_value_selector(item)
        output_dict[key].append(value)

    return output_dict

def flatmap(f: Callable[[T1], Iterable[T2]], l: Iterable[T1]) -> List[T2]:
    """
    Apply the given function to each element of the given iterable, and
    flatten the result.
    """
    return [x for y in l for x in f(y)]

def flatten(l: List[List[T1]]) -> List[T1]:
    """
    Flatten the given list of lists.
    """
    return [item for sublist in l for item in sublist]


# From https://stackoverflow.com/a/1724723/5932184
def find_all(name: str, path: str = ".") -> List[str]:
    """
    Find all files in path (including subdirectories) with 'name' contained within the file name.

    :param name: The name to search for
    :param path: The path to search in (defaults to current directory)
    :return: A list of full file paths
    """
    result = []
    for root, _, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result


def find_all_regex(regex_pattern: str, path: str = ".") -> List[str]:
    """
    Find all files in path (including subdirectories) matching the given regex.

    :param regex_pattern: The regex to search for
    :param path: The path to search in (defaults to current directory)
    :return: A list of full file paths
    """
    regex = re.compile(regex_pattern)
    result = []
    for root, _, files in os.walk(path):
        for file in files:
            if regex.search(file):
                result.append(os.path.join(root, file))
    return result


def read_tsv(file_path: str, delim: str="\t", skip: int=0) -> List[List[str]]:
    """
    Read a tsv file, returning list of list of strings. The final stirng does
    not contain the new line character. Reads the file as UTF-8.
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            return [line.split(delim) for line in file.read().splitlines()][skip:]
    except FileNotFoundError:
        print("File not found: '{}'".format(file_path), file=sys.stderr)
        raise
    except UnicodeDecodeError:
        print("Unable to read file '{}' as UTF-8".format(file_path), file=sys.stderr)
        raise
    except Exception:
        print("Unable to read file '{}'".format(file_path), file=sys.stderr)
        raise

def read_tsv_standard_input(delim: str = "\t", skip: int = 0) -> List[List[str]]:
    """
    Read a tsv file from standard input, returning list of list of strings.
    """
    return [line.split(delim) for line in sys.stdin.read().splitlines()][skip:]

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


def york_tools_model_coefficents(twb: float, ct_range: float, lg_ratio: float):
    """
    Purpose is to build coefficients matching the YorkTools cooling tower model.
    """
    r = ct_range
    lg = lg_ratio
    coeffs = [
        1,                           # 0
        twb,                         # 1
        twb * twb,                   # 2
        r,                           # 3
        twb * r,                     # 4
        twb * twb * r,               # 5
        r * r,                       # 6
        twb * r * r,                 # 7
        twb * twb * r * r,           # 8
        lg,                          # 9
        twb * lg,                    # 10
        twb * twb * lg,              # 11
        r * lg,                      # 12
        twb * r * lg,                # 13
        twb * twb * r * lg,          # 14
        r * r * lg,                  # 15
        twb * r * r * lg,            # 16
        twb * twb * r * r * lg,      # 17
        lg * lg,                     # 18
        twb * lg * lg,               # 19
        twb * twb * lg * lg,         # 20
        r * lg * lg,                 # 21
        twb * r * lg * lg,           # 22
        twb * twb * r * lg * lg,     # 23
        r * r * lg * lg,             # 24
        twb * r * r * lg * lg,       # 25
        twb * twb * r * r * lg * lg, # 26
     ]
    return coeffs

def haystack_commit_update_zinc_meta() -> str:
    """
    Return the Zinc metadata for a commit update. No newline.
    """
    return 'ver: "3.0" commit: "update"'

