import unittest

from pyalgs.data_structures.commons.stack import LinkedListStack
from pyalgs.data_structures.commons.stack import ArrayStack
from pyalgs.data_structures.commons.stack import Stack


class StackTest(unittest.TestCase):
    def test_push(self):
        stack = Stack.create()
        stack.push(10)
        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(2, stack.size())
        self.assertEqual(1, stack.pop())
        self.assertFalse(stack.is_empty())
        self.assertEqual(1, stack.size())
        self.assertEqual(10, stack.pop())
        self.assertTrue(stack.is_empty())


class LinkedListStackTest(unittest.TestCase):
    def test_push(self):
        stack = LinkedListStack()
        stack.push(10)
        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(2, stack.size())
        self.assertEqual(1, stack.pop())
        self.assertFalse(stack.is_empty())
        self.assertEqual(1, stack.size())
        self.assertEqual(10, stack.pop())
        self.assertTrue(stack.is_empty())


class ArrayStackTest(unittest.TestCase):
    def test_push(self):
        stack = ArrayStack()
        stack.push(10)
        self.assertFalse(stack.is_empty())
        self.assertEqual(1, stack.size())
        self.assertEqual(10, stack.pop())
        self.assertTrue(stack.is_empty())


if __name__ == '__main__':
    unittest.main()
