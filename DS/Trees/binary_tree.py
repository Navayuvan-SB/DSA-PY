class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data is None:
            return

        if self.data is None:
            self.data = data
            return

        if self.data >= data:
            if self.left is None:
                self.left = BinaryTreeNode(data)
                return
            return self.left.insert(data)

        if self.data < data:
            if self.right is None:
                self.right = BinaryTreeNode(data)
                return
            return self.right.insert(data)

    def traverse_preorder(self, root):
        result = []

        if root is None:
            return []

        result.append(root.data)

        if root.left:
            result += self.traverse_preorder(root.left)

        if root.right:
            result += self.traverse_preorder(root.right)

        return result

    def traverse_postorder(self, root):
        result = []

        if root is None:
            return []

        if root.left:
            result += self.traverse_postorder(root.left)

        if root.right:
            result += self.traverse_postorder(root.right)

        result.append(root.data)

        return result

    def traverse_inorder(self, root):
        result = []

        if root is None:
            return []

        if root.left:
            result += self.traverse_inorder(root.left)

        result.append(root.data)

        if root.right:
            result += self.traverse_inorder(root.right)

        return result

    def search(self, root, value):
        if root is None:
            return False

        if root.data == value:
            return True

        return self.search(root.left, value) or self.search(root.right, value)
