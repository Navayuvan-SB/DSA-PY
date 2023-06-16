import unittest
from DS.Trees.binary_tree import BinaryTreeNode


class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTreeNode()

    def test_insert_when_empty(self):
        self.root.insert(1)
        self.assertEqual(self.root.traverse_inorder(self.root), [1])

    def test_insert_left_when_not_empty(self):
        self.root.insert(2)
        self.root.insert(1)
        self.assertEqual(self.root.traverse_inorder(self.root), [1, 2])

    def test_insert_right_when_not_empty(self):
        self.root.insert(2)
        self.root.insert(1)
        self.root.insert(3)
        self.assertEqual(self.root.traverse_inorder(self.root), [1, 2, 3])

    def test_inorder_traversal(self):
        self._generate_tree()

        self.assertEqual(self.root.traverse_inorder(self.root), [5, 10, 20, 21, 25])

    def test_preorder_traversal(self):
        self._generate_tree()

        self.assertEqual(self.root.traverse_preorder(self.root), [20, 5, 10, 21, 25])

    def test_postorder_traversal(self):
        self._generate_tree()

        self.assertEqual(self.root.traverse_postorder(self.root), [10, 5, 25, 21, 20])

    def test_search_found(self):
        self._generate_tree()
        self.assertTrue(self.root.search(self.root, 5))

    def test_search_not_found(self):
        self._generate_tree()
        self.assertFalse(self.root.search(self.root, 50))

    def _generate_tree(self):
        self.root.insert(20)
        self.root.insert(21)
        self.root.insert(25)
        self.root.insert(5)
        self.root.insert(10)


if __name__ == "__main__":
    unittest.main()
