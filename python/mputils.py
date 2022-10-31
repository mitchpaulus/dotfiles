import os
from typing import List, Union, Iterable, TypeVar, Callable, Dict, Any, cast
import re
import math
import sys
import subprocess
import hashlib

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
        for file in files:
            if name in file:
                result.append(os.path.join(root, file))
    return result

def find_all_ext(ext: str, path: str = ".") -> List[str]:
    """
    Find all files in path (including subdirectories) with 'name' contained within the file name.

    :param name: The name to search for
    :param path: The path to search in (defaults to current directory)
    :return: A list of full file paths
    """
    # Force an extension to start with a dot
    if len(ext) == 0 or ext[0] != ".":
        ext = "." + ext
    result = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                result.append(os.path.join(root, file))
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
    #  return [convert_to_int_if_possible(c) for c in re.split('([0-9]+)', s) if convert_to_int_if_possible(c) != ""]
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

def version_sort_by(l: Iterable[T1], key_selector: Callable[[T1], str]) -> List[T1]:
    """
    Sort the given iterable in the way that humans expect.
    """
    return sorted(l, key = lambda x: alphanum_key(key_selector(x)))

def version_sort_in_place(l: List[str]):
    """ Sort the given list in the way that humans expect."""
    l.sort(key=alphanum_key)

def version_sort_by_in_place(l: List[T1], key_selector: Callable[[T1], str]):
    """
    Sort the given list in the way that humans expect.
    """
    l.sort(key = lambda x: alphanum_key(key_selector(x)))

def percentile(array: List[float], percent: float) -> float:
    """
    Returns the percentile of the list of data.
    See https://en.wikipedia.org/wiki/Percentile, Nearest-Rank method.
    Definition from Wikipedia:
    One definition of percentile, often given in texts,
    is that the P-th percentile (0<P<=100) of a list of N ordered values (sorted from least to greatest)
    is the smallest value in the list such that no more than P percent of the data is strictly less than the value
    and at least P percent of the data is less than or equal to that value.
    This is obtained by first calculating the ordinal rank and then taking the value from the ordered list that corresponds to that rank.
    :param array: List of data
    :param percent: Percentile to return (0-100)
    """
    index = math.ceil((percent / 100) * len(array))
    # Clamp index between 0 and len(array)
    index = max(1, min(index, len(array) - 1))

    return sorted(array)[index - 1]

def median(array: List[float]) -> float:
    if len(array) == 0:
        raise ValueError("Cannot calculate median of empty list")

    sorted_array = sorted(array)
    if len(sorted_array) % 2 == 0:
        return (sorted_array[len(sorted_array) // 2 - 1] + sorted_array[len(sorted_array) // 2]) / 2
    else:
        return sorted_array[len(sorted_array) // 2]

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

def levenshtein(s1, s2):
    """
    Use levenshtein distance to find the closest match for strings
    Source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
    """
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def first(iterable: Iterable[T1], predicate: Callable[[T1], bool]) -> Union[T1, None]:
    """
    Return the first element in the given iterable that matches the given predicate, or None if no element matches.
    """
    for x in iterable:
        if predicate(x):
            return x
    return None

def sanitize_fn(fn: str) -> str:
    """
    Return a sanitized version of the given filename.
    """
    sanitized = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', fn)
    # Remove multiple underscores in a row
    sanitized = re.sub(r'_{2,}', '_', sanitized)
    # Remove underscores at the beginning or end
    sanitized = re.sub(r'^_|_$', '', sanitized)
    return sanitized

def dirs(path = None) -> List[str]:
    """
    Return a list of all directories in the given path. In version sorted order.
    """
    if path is None:
        path = os.getcwd()
    dirs = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
    version_sort_in_place(dirs)
    return dirs

def files(path = None) -> List[str]:
    """
    Return a list of all files in the given path. In version sorted order.
    """
    if path is None:
        path = os.getcwd()
    files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    version_sort_in_place(files)
    return files

def csv_headers(file: str) -> List[str]:
    """
    Return the headers of the given CSV file. This does not handle quoted headers.
    """
    # Read the first line of the file
    datetime_like_columns = set(['date', 'time', 'datetime', 'timestamp', 'time stamp'])
    if isinstance(file, str):
        with open(file, 'r') as f:
            line = f.readline()
            headers = [f.strip() for f in line.strip().split(',') if f.lower().strip() not in datetime_like_columns]
        return headers
    else:
        raise ValueError("Expected file path as input, got {}".format(type(file)))

def excelchop(filepath: str, worksheet = None, excel_range: str = None, selector = None):
    """
    Run external command 'excelchop', capturing stdout
    """
    args = []

    if worksheet is not None:
        args.append('-w')
        args.append(worksheet)

    if excel_range is not None:
        args.append('-r')
        args.append(excel_range)

    args.append('-A')
    args.append(filepath)

    result = subprocess.run(['excelchop'] + args, capture_output=True)

    if result.returncode != 0:
        raise Exception("excelchop failed with return code {}".format(result.returncode))

    if selector is None:
        selector = lambda line: line.split('\t')

    lines = []
    # Loop over all lines
    for line in result.stdout.decode('utf-8').splitlines(keepends=False):
        lines.append(selector(line))

    return lines

def safe_fn(file_path_to_try):
    # Check if path exists
    if not os.path.exists(file_path_to_try):
        return file_path_to_try

    # Append a number to the end of the file. Use a heuristic to test whether it should have underscore (_1) or space before (1).
    # If the file path has an underscore, use underscore.
    # If the file path has a space, use space and parenthesis.
    # If the file path has neither, use underscore.
    # If the file path has both, use space and parenthesis.
    filename, ext = os.path.splitext(os.path.basename(file_path_to_try))
    if '_' in file_path_to_try:
        # look for existing _1, _2, etc.
        match = re.search(r'_(\d+)$', filename)
        if match:
            # Increment the number
            filename = re.sub(r'_(\d+)$', '_{}'.format(int(match.group(1)) + 1), filename)
        else:
            # Add _1
            filename = '{}_1'.format(filename)
    elif ' ' in file_path_to_try:
        # look for existing (1), (2), etc.
        match = re.search(r'\((\d+)\)$', filename)
        if match:
            # Increment the number
            filename = re.sub(r'\((\d+)\)$', '({})'.format(int(match.group(1)) + 1), filename)
        else:
            # Add (1)
            filename = '{} (1)'.format(filename)
    else:
        # Add _1
        filename = '{}_1'.format(filename)

    return os.path.join(os.path.dirname(file_path_to_try), filename + ext)

def sha256(filepath) -> str:
    """
    Return the SHA256 hash of the given file.
    """
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def resolve_path(relative_path: str, base_path: str = None, separator = None) -> str:
    """
    Resolve the given relative path to an absolute path.
    """
    # raise exception if either relative_path or base_path are empty
    if not relative_path or not base_path:
        raise ValueError("relative_path and base_path must be non-empty")

    # First split on either '/' or '\'
    relative_path_parts: List[str]  = re.split(r'[/\\]', relative_path)

    if base_path is None:
        base_path = os.getcwd()

    base_path_parts: List[str] = re.split(r'[/\\]', base_path)
    # Remove any trailing empty parts
    while base_path_parts and not base_path_parts[-1]:
        base_path_parts.pop()

    for part in relative_path_parts:
        if part == '.':
            continue
        elif part == '..':
            try:
                base_path_parts.pop()
            except IndexError:
                raise ValueError(f"Attempted to resolve path '{relative_path}' relative to '{base_path}', but {relative_path} is outside of {base_path}")
        elif part.strip() == '':
            continue
        else:
            base_path_parts.append(part)

    if separator is None:
        # Combine back with whatever separator was used most.
        count_forward_slash = relative_path.count('/') + base_path.count('/')
        count_back_slash = relative_path.count('\\') + base_path.count('\\')
        if count_forward_slash >= count_back_slash:
            separator = '/'
        else:
            separator = '\\'

    return separator.join(base_path_parts)
