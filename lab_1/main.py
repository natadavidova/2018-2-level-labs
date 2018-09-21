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


def filter_stop_words() -> dict:
    """
    Removes all stop words from the given frequencies dictionary
    """
    pass

def get_top_n() -> tuple:
    """
    Takes first N popular words
    """
    pass
