import unittest
from DS.queue import Queue


class QueueTest(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        self.q.enqueue(1)

    def test_enqueue(self):
        self.q.enqueue(2)
        self.assertListEqual([1, 2], self.q.get_queue())

    def test_dequeue(self):
        self.q.enqueue(2)
        popped_element = self.q.dequeue()

        self.assertEqual(1, popped_element)
        self.assertEqual([2], self.q.get_queue())

    def test_enqueue_overflow(self):
        self.q = Queue(1)
        self.q.enqueue(1)

        self.assertRaisesRegex(Exception, "overflow", self.q.enqueue, 2)

    def test_dequeue_underflow(self):
        self.q = Queue(1)
        self.q.enqueue(1)
        self.assertListEqual([1], self.q.get_queue())

        self.q.dequeue()
        self.assertRaisesRegex(Exception, "underflow", self.q.dequeue)

    def test_is_full(self):
        self.q = Queue(1)
        self.assertEqual(self.q.isFull(), False)

        self.q.enqueue(1)
        self.assertEqual(self.q.isFull(), True)

    def test_is_empty(self):
        self.q = Queue(1)
        self.assertEqual(self.q.isEmpty(), True)

        self.q.enqueue(1)
        self.assertEqual(self.q.isEmpty(), False)


if __name__ == "__main__":
    unittest.main()
