"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)


def propose_candidates(word: str, max_depth_permutations: int = 1) -> list:

    if not word:
        return []

    if not isinstance(max_depth_permutations, int):
        return []

    if max_depth_permutations <= 0:
        return []

    candidates = []

    for letter in range(97, 123):
        for place in range(len(word) + 1):
            new_word = word[:place] + str(chr(letter)) + word[place:]
            if new_word not in candidates:
                candidates.append(new_word)

        for place in range(len(word)):
            new_word = word[:place] + str(chr(letter)) + word[place + 1:]
            if new_word not in candidates:
                candidates.append(new_word)

    for place in range(len(word)):
        new_word = word[:place] + word[place + 1:]
        if new_word not in candidates:
            candidates.append(new_word)

    for place in range(1, len(word)):
        left = word[:place - 1] + word[place]
        right = word[place - 1] + word[place + 1:]
        new_word = left + right
        if new_word not in candidates:
            candidates.append(new_word)

    return candidates


def keep_known(candidates: tuple, frequencies: dict) -> list:

    new_candidates = []

    if not candidates or not isinstance(candidates, tuple) or not frequencies:
        return []

    freq_dict_new = frequencies.copy()

    for key in frequencies.keys():
        if not isinstance(key, str):
            freq_dict_new.pop(key)

    for word in candidates:
        if word in freq_dict_new:
            new_candidates.append(word)
        else:
            if word in freq_dict_new:
                new_candidates.append(word)

    return new_candidates


def choose_best(frequencies: dict, candidates: tuple) -> str:
    max_freq = 0
    max_word = ''

    if not candidates or not frequencies:
        return "UNK"

    frequencies_new = frequencies.copy()

    for key in frequencies.keys():
        if not isinstance(key, str):
            frequencies_new.pop(key)

    for word in candidates:
        if word in frequencies_new:
            # надо проверить по алфавиту
            if int(frequencies_new[word]) == max_freq:
                if word < max_word:
                    max_freq = int(frequencies_new[word])
                    max_word = word
            if int(frequencies_new[word]) > max_freq:
                max_freq = int(frequencies_new[word])
                max_word = word

    return max_word


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if not frequencies:
        return "UNK"

    if frequencies is None:
        return "UNK"

    if as_is_words is not None and isinstance(as_is_words[0], str):

        as_is_words_new = as_is_words[:]

        if isinstance(as_is_words_new, tuple):
            as_is_words_new = list(as_is_words_new)
        else:
            as_is_words_new = [as_is_words_new]

        for index, as_is_word in enumerate(as_is_words):
            if not isinstance(as_is_word, str):
                del(as_is_words_new[index])

        for index, as_is in enumerate(as_is_words_new):
            as_is_words_new[index] = as_is.lower()

        if word in as_is_words_new:
            return word

    if word in frequencies:
        return word

    candidates = propose_candidates(word)
    new_candidates = tuple(keep_known(tuple(candidates), frequencies))
    good_word = choose_best(frequencies, new_candidates)

    return good_word


def spell_check_text(frequencies: dict, as_is_words: tuple, text: str) -> str:

    if not text:
        return ""

    line = ""
    text_new = ""

    if isinstance(text, str):
        words = []
        new_words = []
        need_check_words = {}

        lines = text.split('\n')
        for index in range(len(lines)):
            lines[index] += ' \n'

        for line in lines:
            words += line.split(" ")

        for index, word in enumerate(words):
            symbol = ""
            new_word = ""

            if not word.isalpha():
                for i in word:

                    if i == "'" and new_word or i.isalpha():
                        new_word += i
                    else:
                        symbol = i
                if new_word:
                    new_words.append(new_word)
                if symbol:
                    new_words.append(symbol)
            else:
                new_words.append(word)

        for index, word in enumerate(new_words):
            if not word.lower() in frequencies and word.isalpha():
                need_check_words[word] = index

        for bad_word in need_check_words:
            bad_word_l = bad_word.lower()
            good_word = spell_check_word(frequencies, as_is_words, bad_word_l)
            if not bad_word.islower():
                good_word = good_word[0].upper() + good_word[1:]
            index = need_check_words.get(bad_word)
            new_words[index] = good_word

        for word in new_words:
            if word != '\n':
                if word.isalpha() or "'" in word:
                    line += word + " "
                else:
                    line = line[:-1] + word + " "
            else:
                text_new += line + '\n'
                line = ""

    return text_new
