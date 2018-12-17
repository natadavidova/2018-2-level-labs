import re
import math
from typing import List
import nltk.data
from nltk import tokenize
nltk.download('punkt')


def clean_tokenize_corpus(texts: str) -> list:
    if not texts or not isinstance(texts, list):
        return []
    res_list = []
    for text in texts:
        if not text or not isinstance(text, str):
            continue
        clean_tag_regex = re.compile('<\s*[^>]*>')
        text = clean_tag_regex.sub(' ', text)
        text = text.replace('!', '')
        s_list = []
        sentences = tokenize.sent_tokenize(text)
        regex = re.compile('[^a-zA-Z0-9 ]')
        for sentence in sentences:
            words_list = []
            sentence = regex.sub('', str(sentence))
            words_list.extend(sentence.split(' '))
            s_list.extend(list(map(lambda x: x.lower(), filter(lambda x: x != '', words_list))))
        res_list.append(s_list)
    return res_list


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.tf_idf_values = []
        self.idf_values = {}

    def calculate_tf(self):
        if self.corpus:
            for corp in self.corpus:
                if not corp:
                    continue
                len_corp = len(corp)
                for word in corp:
                    if not isinstance(word, str):
                        len_corp -= 1
                tf = {
                    word: corp.count(word) / len_corp for word in corp if isinstance(word, str)
                }
                self.tf_values.append(tf)
        return self.tf_values

    def calculate_idf(self):
        if self.corpus:
            for corp in self.corpus:
                if corp:
                    new_corp = [item for item in corp if isinstance(item, str)]
                    words_count = dict()
                    for word in new_corp:
                        word_count = sum([int(word in text) for text in self.corpus if text])
                        if words_count != 0:
                            self.idf_values[word] = math.log(len([i for i in self.corpus if i]) / word_count)
        return self.idf_values

    def calculate(self):
        if not self.tf_values or not self.idf_values:
            return []
        else:
            for item in self.tf_values:
                tf_idf_values = {
                    word: tf_value * self.idf_values.get(word) for word, tf_value in item.items()
                }
                self.tf_idf_values.append(tf_idf_values)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if not self.tf_idf_values or document_index >= len(self.tf_idf_values):
            return ()
        tf_idf_dict = self.tf_idf_values[document_index]
        if not word in tf_idf_dict:
            return ()
        list_tf_idf = sorted(tf_idf_dict, key=tf_idf_dict.__getitem__, reverse=True)
        return tf_idf_dict.get(word.lower()), list_tf_idf.index(word.lower())


REFERENCE_TEXT = []
if __name__ == '__main__':
    texts = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in texts:
        with open(text, 'r') as f:
            REFERENCE_TEXT.append(f.read())
