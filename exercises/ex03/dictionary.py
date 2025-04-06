"""Practice with dictionary functions"""

__author__: str = "730642386"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """inverts dictionary, switching key and index"""
    invert_dictionary: dict[str, str] = {}
    for key in dictionary:  # use key instead of index
        invert_dictionary[dictionary[key]] = key
    if len(invert_dictionary) < len(dictionary):
        # compare lengths of the lists
        raise KeyError("Error: there is more than one of the same key")
    return invert_dictionary


def count(input: list[str]) -> dict[str, int]:
    """counts reccurence of input strings"""
    count_input: dict[str, int] = {}
    for value in input:
        if value in count_input:
            count_input[value] += 1
        else:
            count_input[value] = 1
    return count_input


def favorite_color(dictionary_color: dict[str, str]) -> str:
    """assesses most frequently occurring input color"""
    colors: dict[str, int] = {}
    for name in dictionary_color:
        if dictionary_color[name] in colors:
            colors[dictionary_color[name]] += 1
        else:
            colors[dictionary_color[name]] = 1
    most_popular_color: str = ""
    max = -1
    for color in colors:
        if colors[color] > max:
            most_popular_color = color
            max = colors[color]
    return most_popular_color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    """Returns length of each string in list"""
    length_dict = {}
    for string in strings:
        length = len(string)
        if length not in length_dict:
            length_dict[length] = set()
        length_dict[length].add(string)
    return length_dict
