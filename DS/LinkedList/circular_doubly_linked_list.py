class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self, value=None):
        self.head = None
        if value is not None:
            self.head = Node(value)

    def isEmpty(self):
        return self.head is None

    def get_last_element(self):
        if self.isEmpty():
            return None

        return self.head.prev

    def insert_last(self, value):
        node = Node(value)

        if self.isEmpty():
            self.head = node
            self.head.next = node
            self.head.prev = node
            return

        last_element = self.get_last_element()

        node.next = self.head
        node.prev = last_element

        self.head.prev = node
        last_element.next = node

    def insert_first(self, value):
        node = Node(value)

        if self.isEmpty():
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head
            return

        node.prev = self.head.prev
        node.next = self.head
        self.head.prev.next = node
        self.head = node

    def insert_after(self, value, data):
        node = Node(value)

        if self.isEmpty():
            self.head = node
            return

        current_element = self.get_element_by_data(data)
        if current_element is None:
            return

        node.next = current_element.next
        node.prev = current_element

        if current_element.next is not None:
            current_element.next.prev = node

        current_element.next = node

    def insert_before(self, value, data):
        node = Node(value)

        if self.isEmpty():
            self.head = node
            return

        current_element = self.get_element_by_data(data)
        if current_element is None:
            return

        node.next = current_element
        node.prev = current_element.prev
        if current_element.prev is None:
            self.head = node
            current_element.prev = node
            return

        current_element.prev.next = node

    def delete_by_data(self, data):
        if self.isEmpty():
            return

        current_element = self.get_element_by_data(data)

        if current_element is None:
            return

        if current_element == self.head:
            return self.delete_first()

        if current_element.prev is not None:
            current_element.prev.next = current_element.next

        if current_element.next is not None:
            current_element.next.prev = current_element.prev

    def delete_first(self):
        if self.isEmpty():
            return

        self.head.prev.next = self.head.next
        self.head.next.prev = self.head.prev
        self.head = self.head.next

    def delete_last(self):
        if self.isEmpty():
            return

        if self.head.next == self.head:
            self.head = None
            return

        last_element = self.get_last_element()
        last_element.prev.next = last_element.next
        last_element.next.prev = last_element.prev

    def get_element_by_data(self, data):
        if self.isEmpty():
            return None

        if self.head.data == data:
            return self.head

        temp = self.head.next
        while temp is not self.head and temp.data != data:
            temp = temp.next

        if temp is self.head:
            return None

        return temp

    def search(self, target):
        if self.isEmpty():
            return None

        if self.head.data == target:
            return True

        if self.head.next == self.head:
            return False

        temp = self.head.next
        while temp is not self.head:
            if temp.data == target:
                return True
            temp = temp.next

        return False

    def to_list(self):
        if self.isEmpty():
            return []

        if self.head.next == self.head:
            return [self.head.data]

        result = [self.head.data]
        temp = self.head.next
        while temp is not self.head:
            result.append(temp.data)
            temp = temp.next

        return result

    def size(self):
        if self.isEmpty():
            return 0

        if self.head.next == self.head:
            return 1

        size = 1
        temp = self.head.next
        while temp is not self.head:
            size += 1
            temp = temp.next

        return size
