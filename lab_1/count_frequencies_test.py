"""
Checks the first lab. Part about the creation of the frequencies dictionary
"""

import unittest

from lab_1 import main


class CountFrequenciesTest(unittest.TestCase):
    """
    Tests dictionary creation
    """

    def test_dummy(self):
        """
        Ideal scenario
    	"""
        self.assertFalse(main.calculate_frequences())
