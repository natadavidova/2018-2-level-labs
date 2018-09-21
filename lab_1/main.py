"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    first_dict = {}
    list_of_marks = [
                    '.', ',', ':', '"', '`', '[', ']',
                    '?', '!', '@', '&', "'", '-',
                    '$', '^', '*', '(', ')',
                    '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
                     ]
    try:
        elements = text.split()
    except AttributeError:
        return first_dict
    for thing in elements:
        if thing.isdigit():
            continue
        for mark in list_of_marks:
            if mark in thing:
                pos_mark = thing.find(mark)
                thing = thing[:pos_mark] + thing[pos_mark + 1:]
            thing = thing.strip(mark)
        thing = thing.lower()
        first_dict[thing] = first_dict.get(thing, 0) + 1
    if '' in first_dict.keys():
        first_dict.pop('')
    return first_dict


def filter_stop_words(first_dict: dict, stop_words: list) -> dict:
    third_dict = {}
    try:
        second_dict = first_dict.copy()
    except AttributeError:
        return {}
    if first_dict is None or stop_words is None:
        return {}
    for stop_word in stop_words:
        if stop_word in second_dict.keys():
            second_dict.pop(stop_word)
    for k in second_dict.keys():
        try:
            if 0 <= k < 0:
                continue
        except TypeError:
            third_dict[k] = first_dict[k]
    return third_dict


def get_top_n(third_dict: dict, n: int) -> tuple:
    """
    Takes first N popular words
    """
    list_of_lists = []
    list_of_top_words = []
    count = 0
    if n < 0:
        return ()
    for k, v in third_dict.items():
        list_of_lists.append([v, k])
    sorted(list_of_lists)
    for item in list_of_lists:
        if count == n:
            break
        list_of_top_words.append(item[1])
        count += 1
    return tuple(list_of_top_words)


