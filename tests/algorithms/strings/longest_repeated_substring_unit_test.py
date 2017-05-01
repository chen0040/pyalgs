import unittest

from pyalgs.algorithms.strings.longest_repeated_substring import LongestRepeatedSubstringSearch


class LongestRepeatedSubstringSearchUnitTest(unittest.TestCase):

    def test_lrs(self):
        start, len = LongestRepeatedSubstringSearch.lrs('Hello World', 'World Record')
        print('Hello World'[start:(start+len+1)])
        self.assertEqual('World', 'Hello World'[start:(start+len+1)])


if __name__ == '__main__':
    unittest.main()