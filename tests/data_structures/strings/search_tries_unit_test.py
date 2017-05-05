import unittest

from pyalgs.data_structures.strings.search_tries import RWaySearchTries


class RWaySearchTriesUnitTest(unittest.TestCase):
    def test_put(self):
        st = RWaySearchTries()

        st.put("one", 1)
        st.put("two", 2)
        st.put("three", 3)
        st.put("six", 6)
        st.put("ten", 10)
        st.put("ten", 10)

        self.assertEqual(1, st.get("one"))
        self.assertEqual(2, st.get("two"))
        self.assertEqual(3, st.get("three"))

        self.assertTrue(st.contains_key("one"))
        self.assertTrue(st.contains_key("two"))

        self.assertEqual(5, st.size())
        self.assertFalse(st.is_empty())

        st.delete("one")
        self.assertFalse(st.contains_key("one"))
        self.assertEqual(4, st.size())

        st.delete("ten")
        self.assertFalse(st.contains_key("ten"))
        self.assertEqual(3, st.size())

        st.delete("three")
        self.assertFalse(st.contains_key("three"))
        self.assertEqual(2, st.size())

        for i in range(100):
            st.put(str(i), i)
            self.assertEqual(i, st.get(str(i)))

        for key in st.keys():
            print(key)

        for i in range(100):
            st.delete(str(i))
            self.assertFalse(st.contains_key(str(i)))

        st.put('there', 2)
        st.put('this', 2)
        print('with prefix t')
        for key in st.keys_with_prefix('t'):
            print(key)


if __name__ == '__main__':
    unittest.main()
