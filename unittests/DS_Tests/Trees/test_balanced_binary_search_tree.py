import unittest
from DS.Trees.balanced_binary_tree import BalancedBinarySearchTree


class BalancedBinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = BalancedBinarySearchTree()

    def test_empty_returns_none(self):
        root = self.tree.fromArray([])
        self.assertIsNone(root)

    def test_returns_balanced_tree_when_given_array(self):
        root = self.tree.fromArray([1, 2, 3, 4, 5, 6, 7])
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7], root.traverse_inorder(root))

        root = self.tree.fromArray([1, 2, 3])
        self.assertListEqual([1, 2, 3], root.traverse_inorder(root))
