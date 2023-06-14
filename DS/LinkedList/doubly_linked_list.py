class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value=None):
        self.head = None
        if value is not None:
            self.head = Node(value)

    def isEmpty(self):
        return self.head is None

    def get_last_element(self):
        if self.isEmpty():
            return None

        element = self.head
        while element.next is not None:
            element = element.next

        return element

    def insert_last(self, value):
        node = Node(value)

        if self.isEmpty():
            self.head = node
            return

        last_element = self.get_last_element()
        last_element.next = node
        node.prev = last_element

    def insert_first(self, value):
        node = Node(value)

        if self.isEmpty():
            self.head = node
            return

        node.next = self.head
        self.head.prev = node
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

        self.head = self.head.next

    def delete_last(self):
        if self.isEmpty():
            return

        current_element = self.head

        while current_element.next is not None:
            current_element = current_element.next

        if current_element.prev is not None:
            current_element.prev.next = None
            return

        self.head = None

    def get_element_by_data(self, data):
        if self.isEmpty():
            return None

        temp = self.head
        while temp and temp.data != data:
            temp = temp.next

        return temp

    def display(self):
        if self.isEmpty():
            return print("list is empty")

        temp = self.head
        while temp is not None:
            print(temp.data, " -> ")
            temp = temp.next

    def search(self, target):
        temp = self.head
        while temp is not None:
            if temp.data == target:
                return True
            temp = temp.next

        return False

    def to_list(self):
        result = []
        temp = self.head
        while temp is not None:
            result.append(temp.data)
            temp = temp.next

        return result

    def size(self):
        size = 0
        temp = self.head
        while temp is not None:
            size += 1
            temp = temp.next

        return size
