from DS.Trees.binary_tree import BinaryTreeNode


class BalancedBinarySearchTree:
    def fromArray(self, array):
        self.array = array
        root = BinaryTreeNode()
        left = 0
        right = len(array) - 1
        if left > right:
            return None
        self.insert_in_balanced_mode(left, right, root)
        return root

    def insert_in_balanced_mode(self, left, right, root):
        mid = (left + right) // 2
        root.data = self.array[mid]

        if left <= mid - 1:
            root.left = BinaryTreeNode()
            self.insert_in_balanced_mode(left, mid - 1, root.left)

        if mid + 1 <= right:
            root.right = BinaryTreeNode()
            self.insert_in_balanced_mode(mid + 1, right, root.right)
