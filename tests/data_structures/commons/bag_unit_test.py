import unittest

from pyalgs.data_structures.commons.bag import Bag


class BagUnitTest(unittest.TestCase):
    def test_bag(self):
        bag = Bag.create()

        bag.add(100)
        bag.add(200)
        bag.add(300)
        bag.add(400)

        print([i for i in bag.iterate()])

        self.assertEqual(4, bag.size())
        self.assertFalse(bag.is_empty())

if __name__ == '__main__':
    unittest.main()
