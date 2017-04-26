import unittest

from pyalgs.data_structures.commons.hashed_set import HashedSetWithSeparateChaining, HashedSet, \
    HashedSetWithLinearProbing


class HashedSetUnitTest(unittest.TestCase):
    def test_binarySearchTree(self):
        set = HashedSet.create()

        set.add("one")
        set.add("two")
        set.add("three")
        set.add("six")
        set.add("ten")
        set.add("ten")


        self.assertTrue(set.contains("one"))
        self.assertTrue(set.contains("two"))

        self.assertEqual(5, set.size())
        self.assertFalse(set.is_empty())

        set.delete("one")
        self.assertFalse(set.contains("one"))
        self.assertEqual(4, set.size())

        set.delete("ten")
        self.assertFalse(set.contains("ten"))
        self.assertEqual(3, set.size())

        set.delete("three")
        self.assertFalse(set.contains("three"))
        self.assertEqual(2, set.size())

        for i in range(100):
            set.add(str(i))
            self.assertTrue(set.contains(str(i)))

        for key in set.iterate():
            print(key)

        for i in range(100):
            set.delete(str(i))
            self.assertFalse(set.contains(str(i)))


class HashedSetWithSeparateChainingUnitTest(unittest.TestCase):
    def test_binarySearchTree(self):
        set = HashedSetWithSeparateChaining()

        set.add("one")
        set.add("two")
        set.add("three")
        set.add("six")
        set.add("ten")
        set.add("ten")

        self.assertTrue(set.contains("one"))
        self.assertTrue(set.contains("two"))

        self.assertEqual(5, set.size())
        self.assertFalse(set.is_empty())

        set.delete("one")
        self.assertFalse(set.contains("one"))
        self.assertEqual(4, set.size())

        set.delete("ten")
        self.assertFalse(set.contains("ten"))
        self.assertEqual(3, set.size())

        set.delete("three")
        self.assertFalse(set.contains("three"))
        self.assertEqual(2, set.size())

        for i in range(100):
            set.add(str(i))
            self.assertTrue(set.contains(str(i)))

        for key in set.iterate():
            print(key)

        for i in range(100):
            set.delete(str(i))
            self.assertFalse(set.contains(str(i)))


class HashedSetWithLinearProbingUnitTest(unittest.TestCase):
    def test_binarySearchTree(self):
        set = HashedSetWithLinearProbing()

        set.add("one")
        set.add("two")
        set.add("three")
        set.add("six")
        set.add("ten")
        set.add("ten")

        self.assertTrue(set.contains("one"))
        self.assertTrue(set.contains("two"))

        self.assertEqual(5, set.size())
        self.assertFalse(set.is_empty())

        set.delete("one")
        self.assertFalse(set.contains("one"))
        self.assertEqual(4, set.size())

        set.delete("ten")
        self.assertFalse(set.contains("ten"))
        self.assertEqual(3, set.size())

        set.delete("three")
        self.assertFalse(set.contains("three"))
        self.assertEqual(2, set.size())

        for i in range(100):
            set.add(str(i))
            self.assertTrue(set.contains(str(i)))

        for key in set.iterate():
            print(key)

        for i in range(100):
            set.delete(str(i))
            self.assertFalse(set.contains(str(i)))


if __name__ == '__main__':
    unittest.main()
