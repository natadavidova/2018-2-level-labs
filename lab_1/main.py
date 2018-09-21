"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""


def calculate_frequences(text: str) -> dict:
    """
    Calculates number of times each word appears in the text
    """
    # Шаг 0. Уберем возможность неверного ввода.
    if text is None or str(text).isdigit():
        dictionary_freq = {}
        return dictionary_freq

    # Шаг 1. Пройдемся по тексту и уберем лишние символы.
    for element in text:
        if element in """1234567890_-=!@#$%^&*()~_+[]{}:;'",./><?""":
            text = text.replace(element, ' ')
            continue
    text = text.lower()
    text = text.split()

    # Шаг 2. Создадим словарь частотности.
    dictionary_freq = {}
    for word in text:
        frequency = text.count(word)
        dictionary_freq[word] = frequency
        continue

    # Шаг 4. Возвращаем полученный, отсортированный словарь частот.
    return dictionary_freq


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    # Шаг 0. Уберем возможность неверного ввода.
    if stop_words is None or frequencies is None:
        return frequencies

    # Шаг 1. Пройдемся по словарю и исключим ненужные слова.
    for key in list(frequencies):
        if str(key).isdigit() or key in stop_words:
            frequencies.pop(key)
            continue

    # Шаг 2. Возвращаем отфильтрованный словарь.
    return frequencies

def get_top_n() -> tuple:
    """
    Takes first N popular words
    """
    pass
