class Node:
    def __init__(self, data=None):
        self.height = 0
        self.data = data
        self.right = None
        self.left = None


class AVLTree:
    def insert(self, data, root):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(data, root.left)

        if data > root.data:
            root.right = self.insert(data, root.right)

        root.height = max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_height(root.left) - self.get_height(root.right)

        if balance > 1 or balance < -1:
            return self.balance_tree(balance, data, root)

        return root

    def delete(self, data, root):
        if root is None:
            return root

        if data < root.data:
            self.delete(data, root.left)

        if data > root.data:
            self.delete(data, root.right)

        if data == root.data:
            if root.left is None:
                root = root.right

            elif root.right is None:
                root = root.left

            elif root.left and root.right:
                least_right_node = self.get_leaset_node(root.right)
                root.data = least_right_node.data
                root.right = self.delete(least_right_node.data, root.right)

        if root is None:
            return root

        root.height = max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_height(root.left) - self.get_height(root.right)

        if balance > 1 or balance < -1:
            return self.balance_tree(balance, data, root)

        return root

    def get_leaset_node(self, root):
        if root is None or root.left is None:
            return root

        self.get_leaset_node(root.left)

    def balance_tree(self, balance, data, root):
        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)

        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)

        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_height(self, root):
        if root is None:
            return 0
        return root.height + 1

    def rotate_left(self, root):
        if root is None:
            return root

        new_root = root.right
        balance_node = new_root.left

        new_root.left = root
        root.right = balance_node

        new_root.height = max(
            self.get_height(new_root.left), self.get_height(new_root.right)
        )
        root.height = max(self.get_height(root.left), self.get_height(root.right))

        return new_root

    def rotate_right(self, root):
        if root is None:
            return root

        new_root = root.left
        balance_node = new_root.right

        new_root.right = root
        root.left = balance_node

        new_root.height = max(
            self.get_height(new_root.left), self.get_height(new_root.right)
        )
        root.height = max(self.get_height(root.left), self.get_height(root.right))

        return new_root

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
