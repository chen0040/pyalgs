import unittest

from pyalgs.data_structures.commons.queue import LinkedListQueue, Queue, ArrayQueue


class QueueUnitTest(unittest.TestCase):

    def test_Queue(self):
        queue = Queue.create()
        queue.enqueue(10)
        self.assertEqual(1, queue.size())
        self.assertFalse(queue.is_empty())
        queue.enqueue(20)
        self.assertEqual(2, queue.size())
        queue.enqueue(30)

        print([i for i in queue.iterate()])

        self.assertEqual(3, queue.size())
        self.assertEqual(10, queue.dequeue())
        self.assertEqual(2, queue.size())
        self.assertEqual(20, queue.dequeue())
        self.assertEqual(1, queue.size())
        self.assertEqual(30, queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_LinkedListQueue(self):
        queue = LinkedListQueue()
        queue.enqueue(10)
        self.assertEqual(1, queue.size())
        self.assertFalse(queue.is_empty())
        queue.enqueue(20)
        self.assertEqual(2, queue.size())
        queue.enqueue(30)

        print([i for i in queue.iterate()])

        self.assertEqual(3, queue.size())
        self.assertEqual(10, queue.dequeue())
        self.assertEqual(2, queue.size())
        self.assertEqual(20, queue.dequeue())
        self.assertEqual(1, queue.size())
        self.assertEqual(30, queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_ArrayQueue(self):
        queue = ArrayQueue()
        queue.enqueue(10)
        self.assertEqual(1, queue.size())
        self.assertFalse(queue.is_empty())
        queue.enqueue(20)
        self.assertEqual(2, queue.size())
        queue.enqueue(30)

        print([i for i in queue.iterate()])

        self.assertEqual(3, queue.size())
        self.assertEqual(10, queue.dequeue())
        self.assertEqual(2, queue.size())
        self.assertEqual(20, queue.dequeue())
        self.assertEqual(1, queue.size())
        self.assertEqual(30, queue.dequeue())
        self.assertTrue(queue.is_empty())

if __name__ == '__main__':
    unittest.main()