"""
Checks the first lab. Part about the creation of the frequencies dictionary
"""

import unittest

from lab_1 import main

sample_text = "The quick brown fox jumps over the lazy dog"
stop_words = ('ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during',
              'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours',
              'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as',
              'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your',
              'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should',
              'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when',
              'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does',
              'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now',
              'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which',
              'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by',
              'doing', 'it', 'how', 'further', 'was', 'here', 'than')


class CountFrequenciesTest(unittest.TestCase):
    """
    Tests dictionary creation
    """

    def test_calculate_frequences_ideal(self):
        """
        Ideal scenario. Good text.
    	"""

        expected_result = {
            'the': 2,
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'over': 1,
            'lazy': 1,
            'dog': 1
        }

        res = main.calculate_frequences(sample_text)
        self.assertEqual(expected_result, res)

    def test_calculate_frequences_digits(self):
        """
        Text with digits
    	"""

        sample_text = '4 8 15 16 23 42 Dharma Initiative'
        expected_result = {
            'dharma': 1,
            'initiative': 1
        }

        res = main.calculate_frequences(sample_text)
        self.assertEqual(expected_result, res)

    def test_calculate_frequences_punctuation(self):
        """
        Text with punctuation marks
    	"""
        sample_text = "The: quick brown fox, 'jumps' over, the *lazy dog ~"
        expected_result = {
            'the': 2,
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'over': 1,
            'lazy': 1,
            'dog': 1
        }
        res = main.calculate_frequences(sample_text)
        self.assertEqual(expected_result, res)

    def test_calculate_frequences_multilines(self):
        """
        Text in several lines
    	"""
        sample_text = """The quick brown \n
         fox jumps \n
        over the lazy \n
         dog"""

        expected_result = {
            'the': 2,
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'over': 1,
            'lazy': 1,
            'dog': 1
        }
        res = main.calculate_frequences(sample_text)
        self.assertEqual(expected_result, res)

    def test_calculate_frequences_multilines_punctuation(self):
        """
        Text in several lines
    	"""
        sample_text = """The quick* brown \n
         "fox" jumps \n
        over~ the, lazy \n
         dog ^ """

        expected_result = {
            'the': 2,
            'quick': 1,
            'brown': 1,
            'fox': 1,
            'jumps': 1,
            'over': 1,
            'lazy': 1,
            'dog': 1
        }
        res = main.calculate_frequences(sample_text)
        self.assertEqual(expected_result, res)

    def test_calculate_frequences_right_count(self):
        """
        Check counting
    	"""
        sample_text = "a a a a b b b c c d"

        expected_result = {
            'a': 4,
            'b': 3,
            'c': 2,
            'd': 1
        }
        res = main.calculate_frequences(sample_text)
        self.assertEqual(expected_result, res)

    def test_calculate_frequences_empty(self):
        """
        Text is empty
    	"""
        expected_result = {}
        res = main.calculate_frequences('')
        self.assertEqual(expected_result, res)

    def test_calculate_frequences_none(self):
        """
        Text is None
    	"""
        expected_result = {}
        res = main.calculate_frequences(None)
        self.assertEqual(expected_result, res)

    def test_calculate_frequences_not_string(self):
        """
        Text is int
    	"""
        expected_result = {}
        res = main.calculate_frequences(1)
        self.assertEqual(expected_result, res)

    def test_calculate_frequences_inapropriate_symbols_only(self):
        """
        Text is dirty
    	"""
        sample_text = """
        @ 3 $ % \n
        * & ^%$ """
        expected_result = {}
        res = main.calculate_frequences(sample_text)
        self.assertEqual(expected_result, res)

    def test_calculate_frequences_one_word(self):
        """
        Text is dirty
    	"""
        sample_text = """hi"""
        expected_result = {'hi': 1}
        res = main.calculate_frequences(sample_text)
        self.assertEqual(expected_result, res)


    # def test_calculate_frequences_no_spaces(self):
    #     """
    #     Text is dirty
    # 	"""
    #     sample_text = """one*two,threee^four"""
    #     expected_result = {}
    #     res = main.calculate_frequences(sample_text)
    #     self.assertEqual(expected_result, res)


