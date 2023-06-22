import unittest
from DS.Trees.avl_tree import AVLTree, Node


class AVLTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()
        self.root = None

    def test_insert_on_empty_tree(self):
        self.assertEqual(self.tree.traverse_inorder(self.root), [])
        self.root = self.tree.insert(10, self.root)
        self.assertEqual(self.tree.traverse_inorder(self.root), [10])

    def test_insert_on_balancable_tree(self):
        self.generate_tree([10, 20])

        self.assertEqual(self.root.data, 10)
        self.assertEqual(self.root.right.data, 20)
        self.assertIsNone(self.root.left)

    def test_insert_on_non_balancable_tree_left_rotation(self):
        self.generate_tree([10, 20, 30])

        self.assertEqual(self.root.data, 20)
        self.assertEqual(self.root.left.data, 10)
        self.assertEqual(self.root.right.data, 30)

    def test_insert_on_non_balancable_tree_right_rotation(self):
        self.generate_tree([30, 20, 10])

        self.assertEqual(self.root.data, 20)
        self.assertEqual(self.root.left.data, 10)
        self.assertEqual(self.root.right.data, 30)

    def test_insert_on_non_balancable_tree_right_left_rotation(self):
        self.generate_tree([30, 20, 10, 50, 25, 22])

        self.assertEqual(self.root.data, 25)
        self.assertEqual(self.root.right.data, 30)
        self.assertEqual(self.root.left.data, 20)
        self.assertEqual(self.root.left.right.data, 22)
        self.assertEqual(self.root.left.left.data, 10)
        self.assertEqual(self.root.right.right.data, 50)

    def test_insert_on_non_balancable_tree_left_right_rotation(self):
        self.generate_tree([30, 20, 40, 10, 22, 24])

        self.assertEqual(self.root.data, 22)
        self.assertEqual(self.root.right.data, 30)
        self.assertEqual(self.root.left.data, 20)
        self.assertEqual(self.root.left.left.data, 10)
        self.assertEqual(self.root.right.right.data, 40)
        self.assertEqual(self.root.right.left.data, 24)

    def generate_tree(self, data):
        for i in data:
            self.root = self.tree.insert(i, self.root)

        return self.root
