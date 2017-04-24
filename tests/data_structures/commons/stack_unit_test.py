import unittest

from pyalgs.data_structures.commons.stack import LinkedListStack
from pyalgs.data_structures.commons.stack import ArrayStack


class LinkedListStackTest(unittest.TestCase):
    def test_push(self):
        stack = LinkedListStack()
        stack.push(10)
        stack.push(1)
        self.assertFalse(stack.isEmpty())
        self.assertEqual(2, stack.size())
        self.assertEqual(1, stack.pop())
        self.assertFalse(stack.isEmpty())
        self.assertEqual(1, stack.size())
        self.assertEqual(10, stack.pop())
        self.assertTrue(stack.isEmpty())


class ArrayStackTest(unittest.TestCase):
    def test_push(self):
        stack = ArrayStack()
        stack.push(10)
        self.assertFalse(stack.isEmpty())
        self.assertEqual(1, stack.size())
        self.assertEqual(10, stack.pop())
        self.assertTrue(stack.isEmpty())


if __name__ == '__main__':
    unittest.main()
