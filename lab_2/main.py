"""
Labour work #2
 Check spelling of words in the given  text
"""
from copy import copy
from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''
ACCEPTED_LIST = []

def all_deletes(word: str):
    all_deletes = [word[:i - 1] + word[i:] for i in range(1, len(word))]
    all_deletes.append(word[:len(word) - 1])
    return tuple(set(all_deletes))
   
def insert_letter(word: str):
    word_list = [a for a in word]
    letter_list = [a for a in LETTERS]
    res = list()
    for char in letter_list:
        for i in range(0, len(word_list) + 1):
            tmp = copy(word_list)
            tmp.insert(i, char)
            res.append(''.join(tmp))
    return tuple(set(res))

def replace_letter(word: str):
    word_list = [a for a in word]
    letter_list = [a for a in LETTERS]
    res = list()
    for char in letter_list:
        for i in range(0, len(word_list)):
            tmp = copy(word_list)
            tmp[i] = char
            res.append(''.join(tmp))
    return tuple(set(res))
   
   
def get_replacements(word: str):
    res = list()
    word_list = [a for a in word]
    for i in range(0, len(word_list)-1):
        tmp = copy(word_list)
        tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
        res.append(''.join(tmp))
    return tuple(set(res))
   
def propose_candidates(word: str, max_depth_permutations: int=1) -> list:
    if word == '' or word is None:
        return []
    if not max_depth_permutations or max_depth_permutations <= 0:
        return []
    replacements = list()
    replacements.extend(all_deletes(word))
    replacements.extend(insert_letter(word))
    replacements.extend(replace_letter(word))
    replacements.extend(get_replacements(word))
    if max_depth_permutations > 1:
        for i in range(0, max_depth_permutations-1):
            for w in replacements:
                replacements.extend(propose_candidates(w))
    return tuple(set(replacements))
   
def keep_known(candidates: list, accepted: list, freq: dict ):
    if not isinstance(candidates, tuple):
        return []
    if accepted is None:
        return []
    else:
        accepted = tuple(map(lambda x: str(x).lower(), accepted))
    if not freq:
        return []
    if not candidates:
        return []
    res = list()
    if not freq and not accepted:
        return candidates
    accepted = tuple((a for a in accepted if a is not None))
    for c in candidates:
        if c in freq or c in accepted:
            res.append(c)
    return res
   
def choose_best(frequencies: dict, candidates: tuple) -> str:
    if not frequencies:
        return 'UNK'
    if not candidates:
        return 'UNK'
    cand_freq = {c: frequencies.get(c) for c in candidates}
    cand_freq = {item: value for item, value in cand_freq.items() if value is not None}
    if not cand_freq:
        return 'UNK'
    max_candidate = max(cand_freq, key=cand_freq.get)
    return max_candidate
   
def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if word is None:
        return 'UNK'
    if not frequencies:
        return 'UNK'
    if word in frequencies:
        return word
    else:
        if word in [a.lower() for a in as_is_words if not (a is None or isinstance(a, tuple))]:
            return word
        candidates = propose_candidates(word)
        candidates = keep_known(candidates, as_is_words, frequencies)
        best = choose_best(frequencies, candidates)
        return best

if __name__ == '__main__':
        if REFERENCE_TEXT == '':
        with open('very_big_reference_text.txt', 'r') as f:
            REFERENCE_TEXT = f.read()
    freq = calculate_frequences(REFERENCE_TEXT)
