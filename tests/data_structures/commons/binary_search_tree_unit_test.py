import unittest

from pyalgs.data_structures.commons.binary_search_tree import BinarySearchTree


class BinarySearchTreeUnitTest(unittest.TestCase):
    def test_binarySearchTree(self):
        bst = BinarySearchTree.create()

        bst.put("one", 1)
        bst.put("two", 2)
        bst.put("three", 3)
        bst.put("six", 6)
        bst.put("ten", 10)
        bst.put("ten", 10)

        self.assertEqual(1, bst.get("one"))
        self.assertEqual(2, bst.get("two"))
        self.assertEqual(3, bst.get("three"))

        self.assertTrue(bst.contains_key("one"))
        self.assertTrue(bst.contains_key("two"))

        self.assertEqual(5, bst.size())
        self.assertFalse(bst.is_empty())

        bst.delete("one")
        self.assertFalse(bst.contains_key("one"))
        self.assertEqual(4, bst.size())

        bst.delete("ten")
        self.assertFalse(bst.contains_key("ten"))
        self.assertEqual(3, bst.size())

        bst.delete("three")
        self.assertFalse(bst.contains_key("three"))
        self.assertEqual(2, bst.size())

        for i in range(100):
            bst.put(str(i), i)
            self.assertEqual(i, bst.get(str(i)))

        for key in bst.keys():
            print(key)

        for i in range(100):
            bst.delete(str(i))
            self.assertFalse(bst.contains_key(str(i)))




class RedBlackTreeUnitTest(unittest.TestCase):
    def test_binarySearchTree(self):
        bst = BinarySearchTree.create_red_black_tree()

        bst.put("one", 1)
        bst.put("two", 2)
        bst.put("three", 3)
        bst.put("six", 6)
        bst.put("ten", 10)
        bst.put("ten", 10)

        self.assertEqual(1, bst.get("one"))
        self.assertEqual(2, bst.get("two"))
        self.assertEqual(3, bst.get("three"))

        self.assertTrue(bst.contains_key("one"))
        self.assertTrue(bst.contains_key("two"))

        self.assertEqual(5, bst.size())
        self.assertFalse(bst.is_empty())

        bst.delete("one")
        self.assertFalse(bst.contains_key("one"))
        self.assertEqual(4, bst.size())

        bst.delete("ten")
        self.assertFalse(bst.contains_key("ten"))
        self.assertEqual(3, bst.size())

        bst.delete("three")
        self.assertFalse(bst.contains_key("three"))
        self.assertEqual(2, bst.size())

        for i in range(100):
            bst.put(str(i), i)
            self.assertEqual(i, bst.get(str(i)))

        for key in bst.keys():
            print(key)

        for i in range(100):
            bst.delete(str(i))
            self.assertFalse(bst.contains_key(str(i)))


if __name__ == '__main__':
    unittest.main()