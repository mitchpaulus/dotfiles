import os
from typing import List, Union, Iterable, TypeVar, Callable, Dict, Any, cast, Generator, Set, Tuple, Optional
import re
import math
import sys
import subprocess
import hashlib
import datetime

T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')
T4 = TypeVar('T4')

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

    lower_ext = ext.lower()
    upper_ext = ext.upper()

    result = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(lower_ext) or file.endswith(upper_ext):
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

def write_tsv(file_path: str, data: Iterable[Iterable[str]], delim: str="\t") -> None:
    """
    Write a tsv file, given a list of list of strings. The final string does
    not contain the new line character. Writes the file as UTF-8.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        for line in data:
            file.write(delim.join(line) + "\n")

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
    return [convert_to_int_if_possible(c) for c in re.split('([0-9]+)', s.lower())]

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

def files(path = None, return_full_path = False) -> List[str]:
    """
    Return a list of all file names (non-recursive) in the given path. By default, not full path. In version sorted order.
    """
    if path is None:
        path = os.getcwd()

    files = []
    for x in os.listdir(path):
        full_path = os.path.join(path, x)
        if os.path.isfile(full_path):
            files.append(x if not return_full_path else full_path)

    version_sort_in_place(files)
    return files

def tsv_files(path = None, return_full_path = False) -> List[str]:
    """
    Return a list of all .tsv file names (non-recursive) in the given path. By default, not full path. In version sorted order.
    """
    return [x for x in files(path, return_full_path) if x.endswith('.tsv')]

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

def excelchop(filepath: str, worksheet: Union[str, None] = None, excel_range: Union[str, None] = None, selector: Union[Callable[[List[str]], T1], None] = None, skip:int=0) -> Union[List[List[str]], List[T1]]:
    """
    Run external command 'excelchop', capturing stdout.
    :param filepath: Path to Excel file
    :param worksheet: Worksheet name
    :param excel_range: Excel range
    :param selector: Selector function to apply to each row. Function that takes a list of strings and returns a value.
    :return: Output of excelchop, as a list of list of strings by default. If a selector is provided, the output will be a list of the output of the selector.
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

    lines = []
    # Loop over all lines
    for line in result.stdout.decode('utf-8').splitlines(keepends=False)[skip:]:
        split_line = line.split('\t')
        if selector is not None:
            lines.append(selector(split_line))
        else:
            lines.append(split_line)

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

class Stat:
    def __init__(self, mean: float, median: float, std_dev: float, min_data: float, max_data: float, one_percentile: float, five_percentile: float, twenty_five_percentile: float, seventy_five_percentile: float, ninety_five_percentile: float, ninety_nine_percentile: float):
        self.mean = mean
        self.median = median
        self.std_dev = std_dev
        self.min = min_data
        self.max = max_data
        self.one_percentile = one_percentile
        self.five_percentile = five_percentile
        self.twenty_five_percentile = twenty_five_percentile
        self.seventy_five_percentile = seventy_five_percentile
        self.ninety_five_percentile = ninety_five_percentile
        self.ninety_nine_percentile = ninety_nine_percentile

    def __str__(self):
        lines = [
            f'Mean: {self.mean}\n',
            f'Median: {self.median}\n',
            f'Standard Deviation: {self.std_dev}\n',
            f'Min: {self.min}\n',
            f'Max: {self.max}\n',
            f'1%: {self.one_percentile}\n',
            f'5%: {self.five_percentile}\n',
            f'25%: {self.twenty_five_percentile}\n',
            f'75%: {self.seventy_five_percentile}\n',
            f'95%: {self.ninety_five_percentile}\n',
            f'99%: {self.ninety_nine_percentile}\n',
        ]
        return ''.join(lines)

    def __repr__(self):
        return str(self)


def stats(data: List[float]) -> Stat:
    """
    Return the mean, median, standard deviation, min, and max of the given data.
    """
    if not data:
        raise ValueError("Cannot compute stats on empty data")

    # Calculate mean
    mean = sum(data) / len(data)

    data.sort()
    med = median(data)
    std_dev = math.sqrt(sum([(x - mean) ** 2 for x in data]) / len(data))

    # Calculate 1, 5, 25, 75, 95, and 99 percentiles
    one_percentile = percentile(data, 1)
    five_percentile = percentile(data, 5)
    twenty_five_percentile = percentile(data, 25)
    seventy_five_percentile = percentile(data, 75)
    ninety_five_percentile = percentile(data, 95)
    ninety_nine_percentile = percentile(data, 99)

    return Stat(
        mean=mean,
        median=med,
        std_dev=std_dev,
        min_data=min(data),
        max_data=max(data),
        one_percentile=one_percentile,
        five_percentile=five_percentile,
        twenty_five_percentile=twenty_five_percentile,
        seventy_five_percentile=seventy_five_percentile,
        ninety_five_percentile=ninety_five_percentile,
        ninety_nine_percentile=ninety_nine_percentile,
    )

class Month:
    def __init__(self, year_month: int, month_year: int):
        """
        Create a new Month object. Month is 1-based (1 = January, 2 = February, etc.)
        One of the inputs must be between 1 and 12.
        If both are between 1 and 12, the first one is assumed to be the year and the second one is assumed to be the month.
        """
        if 1 <= month_year <= 12:
            self.year = year_month
            self.month = month_year
        elif 1 <= year_month <= 12:
            self.year = month_year
            self.month = year_month
        else:
            raise ValueError("One of the inputs must be between 1 and 12")

    def __eq__(self, other):
        return self.month == other.month and self.year == other.year

    def __hash__(self):
        return hash((self.month, self.year))

    def __str__(self):
        return f'{self.month}/{self.year}'

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            return self.month < other.month
        else:
            return False

    def __le__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            return self.month <= other.month
        else:
            return False

    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year == other.year:
            return self.month > other.month
        else:
            return False

    def __ge__(self, other):
        if self.year > other.year:
            return True
        elif self.year == other.year:
            return self.month >= other.month
        else:
            return False

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError("Can only add an int to a Month")
        return Month.from_int(self.to_int() + other)

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError("Can only subtract an int from a Month")
        return Month.from_int(self.to_int() - other)

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return self - other

    def to_int(self) -> int:
        """
        Convert this Month to an integer. The integer is 1-based (1 = January, 2 = February, etc.)
        """
        return self.year * 12 + (self.month - 1)

    @staticmethod
    def from_int(month_int: int) -> 'Month':
        """
        Convert an integer to a Month. The integer is 1-based (1 = January, 2 = February, etc.)
        """
        year = month_int // 12
        month = month_int % 12 + 1
        return Month(month, year)

    @staticmethod
    def from_date(date: Union[datetime.date, datetime.datetime]) -> 'Month':
        """
        Convert a date to a Month.
        """
        return Month(date.month, date.year)

    @staticmethod
    def from_str(month_str: str) -> 'Month':
        """
        Convert string to a Month. Use any string of non-numeric characters as the separator.
        If only one of the values is between 1 and 12, assume that is the month. If both are
        between 1 and 12, assume the first is the month.
        """
        month, year = re.split(r'[^0-9]+', month_str)
        month = int(month)
        year = int(year)
        if 1 <= month <= 12:
            return Month(month, year)
        elif 1 <= year <= 12:
            return Month(year, month)
        else:
            raise ValueError("Could not determine month and year from string")

    @staticmethod
    def from_date_str(date_str: str) -> 'Month':
        """
        Convert a date string to a Month. The date string must be in the format YYYY-MM-DD.
        """
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return Month.from_date(date)

    # Create generator for iterating over months
    @staticmethod
    def iter_months(start: 'Month', end: 'Month') -> Generator['Month', None, None]:
        """
        Iterate over months from start to end, inclusive.
        """
        month = start
        while month <= end:
            yield month
            month += 1

    def iter(self, end: 'Month') -> Generator['Month', None, None]:
        """
        Iterate over months from this month to end, inclusive.
        """
        return Month.iter_months(self, end)

def to_md(rows: List[List[Any]]) -> str:
    """
    Convert a list of rows to a markdown table.
    """
    max_cols = max(len(row) for row in rows)

    # Min width is 2
    col_widths = [2] * max_cols

    for row in rows:
        for col, cell in enumerate(row):
            col_widths[col] = max(col_widths[col], len(str(cell)) + 2)

    first_row = True
    output_rows = []
    for row in rows:
        # Left margin of single space, right margin of single space, left justified
        contents = [f' {str(cell).ljust(col_widths[col] - 2)} ' for col, cell in enumerate(row)]

        row_str = "|" +  '|'.join(contents) + "|\n"
        output_rows.append(row_str)
        if first_row:
            # Add header separator
            output_rows.append("|" + "|".join(['-' * col_width for col_width in col_widths]) + "|\n")
            first_row = False

    return ''.join(output_rows)

# Need a naive implementation of DBSCAN algorithm
def dbscan(points: List[T1], distance_metric: Callable[[T1, T1], float], eps: float, min_pts: int) -> Tuple[List[List[T1]], List[T1]]:
    """
    Perform DBSCAN clustering on a list of points. The distance metric must be a function that takes two points and returns
    the distance between them. The eps parameter is the maximum distance between two points to be considered neighbors.
    The min_pts parameter is the minimum number of points that must be within eps of a point to be considered a core point.
    Returns (clusters, noise) where clusters is a list of lists for clusters, and noise is a list of points that were not clustered.
    """
    # This was generated by Copilot
    C = 0
    clusters: List[List[T1]] = []
    noise: List[T1] = []
    # Create list of -2s for labels, length of points
    labels = [-2] * len(points)
    # -2 stands for undefined
    # -1 stands for noise
    for idx in range(len(points)):
        p = points[idx]
        if labels[idx] != -2:
            continue

        neighbor_idxs = []
        for idx2 in range(len(points)):
            q = points[idx2]
            if distance_metric(p, q) <= eps:
                neighbor_idxs.append(idx2)

        if len(neighbor_idxs) < min_pts:
            # Noise
            labels[idx] = -1
            continue
        C += 1
        labels[idx] = C

        seed_stack = set([])
        for idx3 in neighbor_idxs:
            seed_stack.add(idx3)
        seed_stack.remove(idx)

        while len(seed_stack) > 0:
            q = seed_stack.pop()
            if labels[q] == -1:
                labels[q] = C
            elif labels[q] != -2:
                continue
            labels[q] = C
            neighbor_idxs2 = []
            for idx4 in range(len(points)):
                r = points[idx4]
                if distance_metric(points[q], r) <= eps:
                    neighbor_idxs2.append(idx4)
            if len(neighbor_idxs2) >= min_pts:
                for idx5 in neighbor_idxs2:
                    seed_stack.add(idx5)
                seed_stack.remove(q)

    for idx, label in enumerate(labels):
        if label == -1:
            noise.append(points[idx])
        else:
            if len(clusters) < label:
                clusters.append([])
            clusters[label - 1].append(points[idx])

    return clusters, noise

def jaccard_index(set1: Set[T1], set2: Set[T1]) -> float:
    # https://en.wikipedia.org/wiki/Jaccard_index
    # Useful similarity metric for sets.
    # See also: https://stats.stackexchange.com/questions/285367/most-well-known-set-similarity-measures
    return len(set1.intersection(set2)) / len(set1.union(set2))


known_hvac_acronyms = {
    "vfd",
    "chwv",
    "chw",
    "hhw",
    "ahu"
    "rh",
    "hx",
    "oa",
}

hvac_acronym_sets = [
    { "chw", "chilled water" },
    { "ahu", "ah" },
    { "rh", "humidity" },
    { "smk", "smoke" },
    { "alm", "alarm" },
    { "tmp", "temp" },
]

canonicalize_map = {
    "tmp": "temp",
    "alm": "alarm",
    "smk": "smoke",
    "humidity": "rh",
    "fltr": "filter",
    "spd": "speed",
    "spc": "space",
    "cnt": "count",
    "hi": "high",
    "lo": "low",
    "pwr": "power",
    "stpt": "setpoint",
    "vlts": "volts",
    "gv": "govt",
    "allm": "alarm",
    "a": "alarm",
    "pmp": "pump",
}

def canonicalize_acronym(acronym: str) -> str:
    return canonicalize_map.get(acronym, acronym)

class HvacString:
    def __init__(self, string: str) -> None:
        self.string = string

    # Define equality based on hvac_acronym_sets above, case-insensitive, other can be a string as well
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, str) or isinstance(__o, HvacString):
            other = __o.string if isinstance(__o, HvacString) else __o
            other = other.lower().strip()
            # First check for exact match
            this = self.string.lower().strip()
            if this == other:
                return True
            for acronym_set in hvac_acronym_sets:
                if other in acronym_set and this in acronym_set:
                    return True
            return False
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.string)

def split_on_lower_to_upper(string: str) -> List[str]:
    output = []
    current = ""
    for char in string:
        if char.isupper() and current:
            output.append(current)
            current = ""
        current += char
    if current:
        output.append(current)
    return output


def split_upper_to_lower(string: str) -> List[str]:
    # Want to split on going from upper to lower case
    # However, assume that if there is more than 1 upper case letter in a row, it is an acronym
    # and the last capital letter is the start of a new token
    output = []
    current = ""
    for char in string:
        if char.isupper():
            if current and len(current) > 1:
                output.append(current[:-1])
                current = current[-1]
        current += char
    if current:
        output.append(current)
    return output

def to_str_list(s: Union[str, List[str], Iterable[str]]) -> List[str]:
    if isinstance(s, str):
        return [s]
    elif isinstance(s, list):
        for item in s:
            if not isinstance(item, str):
                raise ValueError(f"Expected str or list, got {type(s)}")
        return s
    # Check if s implements __iter__
    elif hasattr(s, "__iter__"):
        return [str(item) for item in s]
    else:
        raise ValueError(f"Expected str or list, got {type(s)}")

def to_list(i: Union[T1, List[T1]]) -> List[T1]:
    if isinstance(i, list):
        return i
    else:
        return [i]

def hvac_string_tokenize(s: Union[str, Iterable[str]]) -> List[str]:
    # The purpose of this method is to tokenize a HVAC point name into tokens.
    initial_list = to_str_list(s)
    first_split = []
    for token in initial_list:
        # Can first split on spaces, any punctuation, and underscores. Anything that is not alphanumeric
        split_on_punc = re.split(r'[^a-zA-Z0-9]+', token)
        first_split.extend(split_on_punc)

    # Then split on going from alphabetic to numeric or vice versa
    second_split = []
    for token in first_split:
        second_split.extend(re.split(r'([0-9]+)', token))

    # Remove empty strings
    second_split = [token for token in second_split if token]

    # Split on any lowercase to uppercase transition
    third_split = []
    for token in second_split:
        third_split.extend(split_on_lower_to_upper(token))

    fourth_split = []
    for token in third_split:
        fourth_split.extend(split_upper_to_lower(token))

    return fourth_split


def count_same_sim_metric(string_one: Union[str, Iterable[str]], string_two: Union[str, Iterable[str]]) -> int:
    string_one_tokens = hvac_string_tokenize(to_str_list(string_one))
    string_two_tokens = hvac_string_tokenize(to_str_list(string_two))

    # Make all lowercase
    string_one_tokens = [canonicalize_acronym(token.lower()) for token in string_one_tokens]
    string_two_tokens = [canonicalize_acronym(token.lower()) for token in string_two_tokens]

    # Count the number of tokens that are the same
    return len(set(string_one_tokens).intersection(set(string_two_tokens)))


def pivot(data: Iterable[T1], row_selector: Callable[[T1], T2], col_selector: Callable[[T1], T3], agg: Callable[[T1], T4]) -> Dict[Tuple[T2, T3], List[T4]]:
    """
    This function takes an iterable, a row and column selector, and a transformation function and returns a dictionary data structure representing the pivot table.

    :param data: The data to pivot:
    :param row_selector: A function that takes an item from data and returns the row value
    :param col_selector: A function that takes an item from data and returns the column value
    """
    output = {}
    for item in data:
        row = row_selector(item)
        col = col_selector(item)
        if (row, col) not in output:
            output[(row, col)] = []
        output[(row, col)].append(agg(item))
    return output


def pivot_to_list(pivot_table: Dict[Tuple[T2, T3], T4]) -> List[List[str]]:
    # Pivot table is a dict of tuples to values
    # Convert to a list of lists
    # First get the unique rows and columns
    rows = set()
    cols = set()
    for (row, col) in pivot_table:
        rows.add(row)
        cols.add(col)

    sorted_rows = version_sort_by(rows, lambda x: str(x))
    sorted_cols = version_sort_by(cols, lambda x: str(x))

    # print header row
    rows = []
    rows.append([""] + [str(s) for s in sorted_cols])

    for row in sorted_rows:
        row_list = [str(row)]
        for col in sorted_cols:
            if (row, col) in pivot_table:
                items = pivot_table[(row, col)]
                row_list.append(", ".join([str(item) for item in items]))
            else:
                row_list.append("")
        rows.append(row_list)
    return rows

def outer_join(iter1: Iterable[T1], iter2: Iterable[T2], iter1_key: Callable[[T1], T3], iter2_key: Callable[[T2], T3]) -> Iterable[Tuple[Union[T1, None], Union[T2, None]]]:
    # Build dictionaries for each iterable, keyed by the key function, value is a list of matches
    dict1 = {}
    dict2 = {}
    keys = set()

    for item in iter1:
        key = iter1_key(item)
        keys.add(key)
        dict1.setdefault(key, []).append(item)

    for item in iter2:
        key = iter2_key(item)
        keys.add(key)
        dict2.setdefault(key, []).append(item)

    for key in keys:
        if key in dict1 and key in dict2:
            for item1 in dict1[key]:
                for item2 in dict2[key]:
                    yield (item1, item2)
        elif key in dict1:
            for item1 in dict1[key]:
                yield (item1, None)
        elif key in dict2:
            for item2 in dict2[key]:
                yield (None, item2)

device_types = set([
    'ahu',
    'bcu',
    'vav',
    'fcu',
    'chwp',
    'cwp',
    'chwpump',
    'cwpump',
    'eafan',
    'btu',
    'mzahu',
    'dd',
    'ddvav',
    'ef',
    'tab',
    'sav',
])

full_device = set([
    'energy consumption meter',
    'chw system'
])


non_devices = set([
    'application',
    'trends',
    'log',
    'logs',
    'ip network',
    'bacnet interface',
    'values',
    'io bus',
])


def device_from_path(path: str, sep="/") -> Optional[str]:
    if len(path) == 0:
        return None

    separated = path.split(sep)

    # Start from end of separated, work backwards
    for i in range(len(separated) - 1, -1, -1):
        item = separated[i]

        lowered = item.lower()

        if lowered in non_devices:
            continue

        if lowered in full_device:
            return item

        if lowered.endswith("vfd"):
            return item

        # Split again on separators: '-', '_', and '.'
        split_item = re.split(r'[ _.-]+', item)

        # Check if first item is in device_types and then check if all remaining items are digits
        if split_item[0].lower() in device_types:
            if all([all([c.isdigit() for c in s]) for s in split_item[1:]]):
                return item

    return None

def true_like(text: str) -> bool:
    clean = str(text).strip().lower()
    if clean in ['true', 'yes', '1', "t", "y"]:
        return True
    elif clean in ['false', 'no', '0', "f", "n", ""]:
        return False
    raise ValueError("Cannot convert {} to boolean".format(text))

class StringBuilder:
    """World's simplest string builder"""
    def __init__(self):
        self._strings = []

    def append(self, value):
        self._strings.append(value)

    def clear(self):
        self._strings = []

    def __str__(self):
        return "".join(self._strings)

def common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


def brent_zero_function(f, a, b, tol=1e-6, max_iter=1000):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must have different signs at the interval endpoints.")

    if abs(f(a)) < abs(f(b)):
        a, b = b, a

    c = a
    mflag = True
    delta = 1e-50
    iter_count = 0

    while iter_count < max_iter and abs(b - a) > tol:
        fa = f(a)
        fb = f(b)
        fc = f(c)
        if fa != fc and fb != fc:
            # Inverse quadratic interpolation
            s = a * fb * fc / ((fa - fb) * (fa - fc)) + b * fa * fc / (
                (fb - fa) * (fb - fc)) + c * fa * fb / ((fc - fa) * (fc - fb))
        else:
            # Secant method
            s = b - fb * (b - a) / (fb - fa)

        # Check if s is within the required bounds
        if (s < (3 * a + b) / 4 or s > b) or (mflag is True and abs(s - b) >= abs(b - c) / 2) or (
                mflag is False and abs(s - b) >= abs(c - d) / 2) or (mflag is True and abs(b - c) < delta) or (mflag is False and abs(c - d) < delta):
            # Bisection method
            s = (a + b) / 2
            mflag = True
        else:
            mflag = False

        d = c
        c = b

        if fa * f(s) < 0:
            b = s
        else:
            a = s

        if abs(fa) < abs(fb):
            a, b = b, a

        iter_count += 1

    if iter_count == max_iter:
        raise RuntimeError("Maximum number of iterations reached before convergence.")

    return b

def annual_facility_electricity(file_path: str) -> float:
    # File path should be relative path to "*.eso" file
    # If not *.eso raise exception

    if not file_path.endswith(".eso"):
        raise ValueError("File path must be to an *.eso file")

    annual_elec = -1
    with open(file_path, 'r') as f:
        for l in f:
            if l.startswith("End of Data Dictionary"):
                break
            split_data = l.strip().split(",")
            if len(split_data) >= 3:
                if split_data[2].startswith("Electricity:Facility [J] !Annual"):
                    annual_elec = int(split_data[0])

        if annual_elec == -1:
            raise ValueError("Could not find annual electricity consumption in file")

        for l in f:
            to_check = str(annual_elec) + ","
            if l.startswith(to_check):
                joules = float(l.split(",")[1])
                return joules/3600000

    raise ValueError(f"Could not find annual electricity consumption '{annual_elec}' in file")

dst_dates = { 2015:(8, 1), 2016:(13, 6), 2017:(12,5), 2018:(11,4), 2019:(10,3), 2020:(8, 1), 2021:(14,7), 2022:(13,6), 2023:(12,5), 2024:(10,3), 2025:(9, 2), 2026:(8, 1), 2027:(14,7), 2028:(12,5), 2029:(11,4), }

def is_dst(year, month, day, hour):
    march_day, november_day = dst_dates[year]

    if month > 3 and month < 11:
        return True
    elif month == 3 and (day > march_day or (day == march_day and hour >= 2)):
        return True
    elif month == 11 and (day < november_day or (day == november_day and hour < 2)):
        return True
    else:
        return False

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_in_month(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    elif month > 0 and month < 13:
        return 31
    else:
        raise(ValueError("Month must be between 1 and 12"))

def days_since_epoch(year: int, month: int, day: int):
    days = 0
    for y in range(1970, year):
        days += 366 if is_leap_year(y) else 365

    for m in range(1, month):
        days += days_in_month(year, m)

    days += day - 1
    return days


def to_unix_timestamp(year: int, month: int, day: int, hour: int, minute: int, second: int) -> int:
    days = days_since_epoch(year, month, day)
    hours = days * 24 + hour
    minutes = hours * 60 + minute
    unix_timestamp = minutes * 60 + second
    return unix_timestamp


def cst_to_unix_timestamp(year, month, day, hour, minute, second):
    # Calculate the Unix timestamp
    days = days_since_epoch(year, month, day)
    hours = days * 24 + hour
    minutes = hours * 60 + minute
    unix_timestamp = minutes * 60 + second

    # Adjust for daylight savings time
    if is_dst(year, month, day, hour):
        # Subtract 5 hour = 5 hr * 60 min/hr * 60 sec/min = 18000 sec
        unix_timestamp += 18000
    else:
        unix_timestamp += 21600

    return unix_timestamp
