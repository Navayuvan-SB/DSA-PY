import unittest
from DS.stack import Stack


class StackTest(unittest.TestCase):
    def setUp(self):
        self.s = Stack()
        self.s.push(1)

    def test_push(self):
        self.s.push(2)
        self.assertListEqual([1, 2], self.s.get_stack())

    def test_pop(self):
        self.s.push(2)
        popped_element = self.s.pop()

        self.assertEqual(2, popped_element)
        self.assertEqual([1], self.s.get_stack())

    def test_peek(self):
        self.s.push(2)
        peak_element = self.s.peek()

        self.assertEqual(2, peak_element)

    def test_push_overflow(self):
        self.s = Stack(1)
        self.s.push(1)

        self.assertRaisesRegex(Exception, "overflow", self.s.push, 2)

    def test_pop_underflow(self):
        self.s = Stack(1)
        self.s.push(1)
        self.assertListEqual([1], self.s.get_stack())

        self.s.pop()
        self.assertRaisesRegex(Exception, "underflow", self.s.pop)

    def test_is_full(self):
        self.s = Stack(1)
        self.assertEqual(self.s.isFull(), False)

        self.s.push(1)
        self.assertEqual(self.s.isFull(), True)

    def test_is_empty(self):
        self.s = Stack(1)
        self.assertEqual(self.s.isEmpty(), True)

        self.s.push(1)
        self.assertEqual(self.s.isEmpty(), False)


if __name__ == "__main__":
    unittest.main()
