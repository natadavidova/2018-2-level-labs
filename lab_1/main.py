"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    first_dict = {}
    list_of_marks = ['.', ',', ':', '"', '`', '[', ']', '?', '!', '@', '&', '$', '^', '*', '(', ')', '-',
                     '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
                     '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "'"
                     ]
    try:
        elements = text.split()
    except:
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
        first_dict[thing] = first_dict.get(thing, 0) + 1  ### Первый ШАГ
    if '' in first_dict.keys():
        first_dict.pop('')
    # for key in first_dict:
    #   print(key, first_dict[key])
    # fictional_stop_words = []
    # for k in first_dict:                    ### Второй ШАГ
    #   thing_2 = str(k)
    #  length = len(thing_2)
    # if length <= 2:
    #    fictional_stop_words.append(k)
    # print(fictional_stop_words)
    # for stop_word in fictional_stop_words:  ### Второй ШАГ
    # if stop_word in first_dict.keys():
    #   first_dict.pop(stop_word)
    ##for key in first_dict:
    #  print(key, first_dict[key])
    return first_dict


def filter_stop_words(first_dict: dict, stop_words: list) -> dict:
    list_of_marks = ['.', ',', ':', '"', '`', '[', ']', '?', '!', '@', '&', '$', '^', '*', '(', ')', '-',
                     '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
                     '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "'"
                     ]
    second_dict = {}
    try:
        second_dict = first_dict.copy()
    except:
        second_dict = {}
    ### Если key присваивается пользователем, key is int
    if first_dict is None or stop_words is None:
        return second_dict
    for stop_word in stop_words:
        if stop_word in second_dict.keys():
            second_dict.pop(stop_word)
    #for key in second_dict:
     #   print(key, second_dict[key])
    # Дополнительные проверки
    return second_dict



def get_top_n() -> tuple:
    """
    Takes first N popular words
    """
    pass
