import unittest

from lab_2.main import spell_check_word


class SpellCheckWordsTest(unittest.TestCase):
    """Checks the whole workflow of all functions"""

    def test_spell_check_word_ideal(self):
        """ideal case all data is as expected """
        freq_dict = dict(list=1, lust=2)
        word = 'lwst'
        expected = 'lust'
        res = spell_check_word(freq_dict, word)
        self.assertEqual(expected, res)

    def test_spell_check_word_dict_none(self):
        freq_dict = None
        word = 'lwst'
        expected = 'UNK'
        res = spell_check_word(freq_dict, word)
        self.assertEqual(expected, res)

    def test_spell_check_word_none(self):
        freq_dict = dict(list=1, lust=2)
        word = None
        expected = 'UNK'
        res = spell_check_word(freq_dict, word)
        self.assertEqual(expected, res)
