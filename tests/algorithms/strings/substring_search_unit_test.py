import unittest

from pyalgs.algorithms.strings.substring_search import BruteForceSubstringSearch, RabinKarp, BoyerMoore, \
    KnuthMorrisPratt
from tests.algorithms.strings.util import some_text


class BruteForceSubstringSearchUnitTest(unittest.TestCase):

    def test_search(self):
        t = some_text()
        ss = BruteForceSubstringSearch('men')
        self.assertNotEqual(-1, ss.search_in(t))
        self.assertEqual(-1, ss.search_in('Hello World'))


class RabinKarpUnitTest(unittest.TestCase):

    def test_search(self):
        t = some_text()
        ss = RabinKarp('men')
        self.assertNotEqual(-1, ss.search_in(t))
        self.assertEqual(-1, ss.search_in('Hello World'))


class BoyerMooreUnitTest(unittest.TestCase):

    def test_search(self):
        t = some_text()
        ss = BoyerMoore('men')
        self.assertNotEqual(-1, ss.search_in(t))
        self.assertEqual(-1, ss.search_in('Hello World'))


class KnuthMorrisPrattUnitTest(unittest.TestCase):

    def test_search(self):
        t = some_text()
        ss = KnuthMorrisPratt('men')
        self.assertNotEqual(-1, ss.search_in(t))
        self.assertEqual(-1, ss.search_in('Hello World'))

if __name__ == '__main__':
    unittest.main()