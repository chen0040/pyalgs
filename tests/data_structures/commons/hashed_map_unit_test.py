import unittest

from pyalgs.data_structures.commons.hashed_map import HashedMapWithSeparateChaining, HashedMap


class HashedMapUnitTest(unittest.TestCase):
    def test_binarySearchTree(self):
        map = HashedMap.create()

        map.put("one", 1)
        map.put("two", 2)
        map.put("three", 3)
        map.put("six", 6)
        map.put("ten", 10)
        map.put("ten", 10)

        self.assertEqual(1, map.get("one"))
        self.assertEqual(2, map.get("two"))
        self.assertEqual(3, map.get("three"))

        self.assertTrue(map.contains_key("one"))
        self.assertTrue(map.contains_key("two"))

        self.assertEqual(5, map.size())
        self.assertFalse(map.is_empty())

        map.delete("one")
        self.assertFalse(map.contains_key("one"))
        self.assertEqual(4, map.size())

        map.delete("ten")
        self.assertFalse(map.contains_key("ten"))
        self.assertEqual(3, map.size())

        map.delete("three")
        self.assertFalse(map.contains_key("three"))
        self.assertEqual(2, map.size())

        for i in range(100):
            map.put(str(i), i)
            self.assertEqual(i, map.get(str(i)))

        for key in map.keys():
            print(key)

        for i in range(100):
            map.delete(str(i))
            self.assertFalse(map.contains_key(str(i)))


class HashedMapWithSeparateChainingUnitTest(unittest.TestCase):
    def test_binarySearchTree(self):
        map = HashedMapWithSeparateChaining()

        map.put("one", 1)
        map.put("two", 2)
        map.put("three", 3)
        map.put("six", 6)
        map.put("ten", 10)
        map.put("ten", 10)

        self.assertEqual(1, map.get("one"))
        self.assertEqual(2, map.get("two"))
        self.assertEqual(3, map.get("three"))

        self.assertTrue(map.contains_key("one"))
        self.assertTrue(map.contains_key("two"))

        self.assertEqual(5, map.size())
        self.assertFalse(map.is_empty())

        map.delete("one")
        self.assertFalse(map.contains_key("one"))
        self.assertEqual(4, map.size())

        map.delete("ten")
        self.assertFalse(map.contains_key("ten"))
        self.assertEqual(3, map.size())

        map.delete("three")
        self.assertFalse(map.contains_key("three"))
        self.assertEqual(2, map.size())

        for i in range(100):
            map.put(str(i), i)
            self.assertEqual(i, map.get(str(i)))

        for key in map.keys():
            print(key)

        for i in range(100):
            map.delete(str(i))
            self.assertFalse(map.contains_key(str(i)))


if __name__ == '__main__':
    unittest.main()
