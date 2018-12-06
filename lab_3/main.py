"""
Labour work #3
 Building an own N-gram model
"""

import re
import math
from typing import List
import nltk.data
from nltk import tokenize
nltk.download('punkt')


class WordStorage:
    def __init__(self):
        self.storage = {}
        self.id = 0

    def put(self, word: str) -> int:
        if not isinstance(word, str):
            return -1
        if word is None or len(word) == 0:
            return -1
        if word in self.storage:
            return self.storage[word]
        self.id += 1
        self.storage[word] = self.id
        return self.id

    def get_id_of(self, word: str) -> int:
        if word not in self.storage:
            return -1
        else:
            return self.storage[word]

    def get_original_by(self, word_id: int) -> str:
        if word_id not in self.storage.values():
            return 'UNK'
        for word, w_id in self.storage.items():
            if w_id == word_id:
                return word

    def from_corpus(self, corpus: tuple):
        if corpus is None or len(corpus) == 0:
            return ()
        elif not isinstance(corpus, tuple):
            return -1
        else:
            for item in corpus:
                self.put(item)


class NGramTrie:
    def __init__(self, size):
        self.size = size
        self.gram_frequencies = {}
        self.gram_log_probabilities = {}

    def fill_from_sentence(self, sentence: tuple) -> str:
        try:
            if not isinstance(sentence, tuple):
                return 'ERROR'
            if len(sentence) == 0:
                return 'ERROR'

            n_grams = [tuple(sentence[i:i + self.size]) for i in range(len(sentence) - self.size + 1)]
            for el in n_grams:
                frequency = n_grams.count(el)
                self.gram_frequencies[el] = frequency
            return 'OK'
        except Exception:
            return 'ERROR'

    def get_equal_gram_sum(self, gram):
        freq_sum = 0
        for g in self.gram_frequencies:
            if gram[0] == g[0]:
                freq_sum += self.gram_frequencies[g]
        return freq_sum

    def calculate_log_probabilities(self):
        for gram, freq in self.gram_frequencies.items():
            equal_sum_freq = self.get_equal_gram_sum(gram)
            probability = freq / equal_sum_freq
            log_probability = math.log(probability)
            self.gram_log_probabilities[gram] = log_probability

    def predict_next_sentence(self, prefix: tuple) -> list:
        if not isinstance(prefix, tuple):
            return []
        if len(prefix) != self.size - 1:
            return []
        prefix_list = list(prefix)
        while True:
            ngrams = []
            for gram in self.gram_log_probabilities:
                if gram[0] == prefix[0]:
                    ngrams.append((self.gram_log_probabilities[gram], gram))
            if len(ngrams) != 0:
                prefix = ((max(ngrams)[1])[1], )
                prefix_list.append(prefix[0])
                ngrams.append(prefix)
            else:
                return prefix_list


def split_by_sentence(text: str) -> list:
    s_list = []
    if not text:
        return s_list
    if ' ' not in text:
        return s_list
    if text and len(text.strip()) > 0:
        sentences = tokenize.sent_tokenize(text)
        regex = re.compile('[^a-zA-Z0-9 ]')
        for sentence in sentences:
            words_list = []
            words_list.append('<s>')
            sentence = regex.sub('', str(sentence))
            words_list.extend(sentence.split(' '))
            words_list.append('</s>')
            s_list.append(list(map(lambda x: x.lower(), filter(lambda x: x != '', words_list))))
    return s_list


def encode(storage_instance, corpus) -> list:
    return [[storage_instance.get_id_of(word) for word in sentence] for sentence in corpus]


if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
    







