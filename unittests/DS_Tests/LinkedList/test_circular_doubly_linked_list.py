import unittest
from DS.LinkedList.circular_doubly_linked_list import CircularDoublyLinkedList, Node


class CircularDoubleLinkedListTest(unittest.TestCase):
    def test_init(self):
        node3 = Node("Node 3")
        node2 = Node("Node 2")
        node1 = Node("Node 1")

        node1.next = node2
        node1.prev = node3

        node2.prev = node1
        node2.next = node3

        node3.prev = node2
        node3.next = node1

        linked_list = CircularDoublyLinkedList()
        linked_list.head = node1

        self.assertEqual(linked_list.head, node1)
        self.assertEqual(linked_list.head.next, node2)
        self.assertEqual(linked_list.head.next.next, node3)

        self.assertEqual(linked_list.head.next.prev, node1)
        self.assertEqual(linked_list.head.next.next.prev, node2)

    def test_to_list(self):
        node3 = Node("Node 3")
        node2 = Node("Node 2")
        node1 = Node("Node 1")

        node1.next = node2
        node1.prev = node3

        node2.prev = node1
        node2.next = node3

        node3.prev = node2
        node3.next = node1

        linked_list = CircularDoublyLinkedList()
        linked_list.head = node1

        self.assertEqual(linked_list.to_list(), [node1.data, node2.data, node3.data])

    def test_to_list_empty(self):
        linked_list = CircularDoublyLinkedList()
        self.assertEqual(linked_list.to_list(), [])

    def test_insert_first(self):
        linked_list = CircularDoublyLinkedList()
        linked_list.insert_first("Hello")
        linked_list.insert_first("World")
        linked_list.insert_first(",")
        linked_list.insert_first("Python is Awesome")

        self.assertEqual(
            linked_list.to_list(), ["Python is Awesome", ",", "World", "Hello"]
        )
        self.assertEqual(linked_list.size(), 4)

    def test_insert_first_1000_nodes(self):
        linked_list = CircularDoublyLinkedList()
        inpt = []
        for i in range(0, 1000):
            linked_list.insert_first(i)
            inpt.append(i)

        inpt.sort(reverse=True)
        self.assertEqual(linked_list.to_list(), inpt)
        self.assertEqual(linked_list.size(), len(inpt))

    def test_insert_last(self):
        linked_list = CircularDoublyLinkedList()
        inpt = []
        for i in range(0, 1000):
            linked_list.insert_last(i)
            inpt.append(i)

        self.assertEqual(linked_list.to_list(), inpt)
        self.assertEqual(linked_list.size(), len(inpt))

    def test_insert_first_None(self):
        linked_list = CircularDoublyLinkedList()
        linked_list.insert_first(None)
        linked_list.insert_first(None)

        self.assertEqual(linked_list.to_list(), [None, None])
        self.assertEqual(linked_list.size(), 2)

    def test_insert_last_None(self):
        linked_list = CircularDoublyLinkedList()
        linked_list.insert_last(None)
        linked_list.insert_last(None)

        self.assertEqual(linked_list.to_list(), [None, None])
        self.assertEqual(linked_list.size(), 2)

    def test_insert_last_list(self):
        linked_list = CircularDoublyLinkedList()
        inpt = ["Hello", "World", "Python is Awesome!"]
        for i in inpt:
            linked_list.insert_last(i)

        self.assertEqual(linked_list.to_list(), inpt)
        self.assertEqual(linked_list.size(), len(inpt))

    def test_insert_last_list(self):
        linked_list = CircularDoublyLinkedList()
        linked_list.insert_last(1)
        linked_list.insert_last(2)
        linked_list.insert_last(3)

        inpt = ["Hello", "World", "Python is Awesome!"]
        for i in inpt:
            linked_list.insert_last(i)

        self.assertEqual(
            linked_list.to_list(), [1, 2, 3, "Hello", "World", "Python is Awesome!"]
        )
        self.assertEqual(linked_list.size(), 6)

    def test_remove_empty(self):
        linked_list = CircularDoublyLinkedList()
        linked_list.delete_first()

        self.assertEqual(linked_list.size(), 0)
        self.assertEqual(linked_list.to_list(), [])

    def test_remove_first_element(self):
        linked_list = CircularDoublyLinkedList()
        inpt = ["Hello", "World", "Python", "Is", "Awesome"]
        for i in inpt:
            linked_list.insert_last(i)
        linked_list.delete_by_data(inpt[0])

        self.assertEqual(linked_list.size(), len(inpt) - 1)
        self.assertEqual(linked_list.to_list(), inpt[1:])

    def test_remove_middle_element(self):
        linked_list = CircularDoublyLinkedList()
        inpt = ["Hello", "World", "Python", "Is", "Awesome"]
        for i in inpt:
            linked_list.insert_last(i)
        linked_list.delete_by_data(inpt[2])

        self.assertEqual(linked_list.size(), len(inpt) - 1)
        self.assertEqual(linked_list.to_list(), inpt[:2] + inpt[3:])

    def test_remove_last_element(self):
        linked_list = CircularDoublyLinkedList()
        inpt = ["Hello", "World", "Python", "Is", "Awesome"]
        for i in inpt:
            linked_list.insert_last(i)
        linked_list.delete_by_data(inpt[-1])

        self.assertEqual(linked_list.size(), len(inpt) - 1)
        self.assertEqual(linked_list.to_list(), inpt[:-1])

    def test_remove_non_existing_element(self):
        linked_list = CircularDoublyLinkedList()
        inpt = ["Hello", "World", "Python", "Is", "Awesome"]
        for i in inpt:
            linked_list.insert_last(i)

        linked_list.delete_by_data("hi")

        self.assertEqual(linked_list.size(), len(inpt))
        self.assertEqual(linked_list.to_list(), inpt)

    def test_pop_empty(self):
        linked_list = CircularDoublyLinkedList()
        self.assertEqual(linked_list.to_list(), [])
        self.assertEqual(linked_list.size(), 0)

    def test_search_empty(self):
        linked_list = CircularDoublyLinkedList()
        self.assertFalse(linked_list.search(1))

    def test_search_first_element(self):
        linked_list = self.make_hundred_elements_linked_list()
        self.assertTrue(linked_list.search(1))

    def test_search_middle_element(self):
        linked_list = self.make_hundred_elements_linked_list()
        self.assertTrue(linked_list.search(50))

    def test_search_last_element(self):
        linked_list = self.make_hundred_elements_linked_list()
        self.assertTrue(linked_list.search(100))

    def test_search_non_existing_element(self):
        linked_list = self.make_hundred_elements_linked_list()
        self.assertFalse(linked_list.search(101))

    def test_insert_empty_list(self):
        linked_list = CircularDoublyLinkedList()
        linked_list.insert_first("Hello")
        self.assertEqual(linked_list.to_list(), ["Hello"])
        self.assertEqual(linked_list.size(), 1)

    def test_insert_first(self):
        linked_list, inpt = self.make_five_elements_linked_list()
        linked_list.insert_first("Hello")
        self.assertEqual(linked_list.to_list(), ["Hello"] + inpt)
        self.assertEqual(linked_list.size(), len(inpt) + 1)

    def test_insert_last(self):
        linked_list, inpt = self.make_five_elements_linked_list()
        linked_list.insert_last("Hello")
        self.assertEqual(linked_list.to_list(), inpt + ["Hello"])
        self.assertEqual(linked_list.size(), len(inpt) + 1)

    def test_insert_middle(self):
        linked_list, inpt = self.make_five_elements_linked_list()
        index_to_insert = 2
        linked_list.insert_after("Hello", 2)
        self.assertEqual(
            linked_list.to_list(),
            inpt[:index_to_insert] + ["Hello"] + inpt[index_to_insert:],
        )
        self.assertEqual(linked_list.size(), len(inpt) + 1)

    def make_hundred_elements_linked_list(self):
        linked_list = CircularDoublyLinkedList()
        for i in range(1, 101, 1):
            linked_list.insert_last(i)
        return linked_list

    def make_five_elements_linked_list(self):
        linked_list = CircularDoublyLinkedList()
        inpt = list(range(1, 6, 1))
        for i in range(1, 6, 1):
            linked_list.insert_last(i)
        return linked_list, inpt


if __name__ == "__main__":
    unittest.main()
