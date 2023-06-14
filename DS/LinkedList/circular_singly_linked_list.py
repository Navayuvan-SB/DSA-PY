class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self, value=None):
        self.head = None
        if value is not None:
            self.head = Node(value)
            self.head.next = self.head

    def isEmpty(self):
        return self.head is None

    def get_last_element(self):
        if self.isEmpty():
            return None

        if self.head.next is None:
            return self.head

        element = self.head.next
        while element.next is not self.head:
            element = element.next

        return element

    def insert_last(self, value):
        node = Node(value)

        if self.isEmpty():
            self.head = node
            self.head.next = self.head
            return

        last_element = self.get_last_element()
        last_element.next = node
        node.next = self.head

    def insert_first(self, value):
        node = Node(value)

        if self.isEmpty():
            self.head = node
            self.head.next = self.head
            return

        last_element = self.get_last_element()

        node.next = self.head
        self.head = node

        last_element.next = node

    def insert_after(self, value, data):
        node = Node(value)

        if self.isEmpty():
            self.head = node
            self.head.next = self.head
            return

        current_element = self.get_element_by_data(data)
        if current_element is None:
            return

        node.next = current_element.next
        current_element.next = node

    def insert_before(self, value, data):
        node = Node(value)

        if self.isEmpty():
            self.head = node
            self.head.next = self.head
            return

        result = self.get_element_and_prev_element_by_data(data)
        prev_element = result["previous_element"]
        current_element = result["current_element"]

        if current_element is None:
            return

        if current_element is self.head:
            return self.insert_first(value)

        prev_element.next = node
        node.next = current_element

    def delete_first(self):
        if self.isEmpty():
            return

        last_element = self.get_last_element()
        self.head = self.head.next
        last_element.next = self.head

    def delete_last(self):
        if self.isEmpty():
            return

        if self.head.next is self.head:
            self.head = None
            return

        prev, temp = None, self.head

        while temp.next is not None:
            prev = temp
            temp = temp.next

        prev.next = temp.next

    def delete_by_data(self, data):
        if self.isEmpty():
            return

        if data is None:
            return

        result = self.get_element_and_prev_element_by_data(data)
        prev_element = result["previous_element"]
        current_element = result["current_element"]

        if current_element is None:
            return

        if current_element is self.head:
            return self.delete_first()

        prev_element.next = current_element.next

    def get_element_by_data(self, data):
        if self.isEmpty():
            return None

        temp = self.head
        while temp and temp.data != data:
            temp = temp.next

        return temp

    def search(self, target):
        if self.isEmpty():
            return False

        if self.head.data == target:
            return True

        if self.head.next is self.head:
            return False

        temp = self.head.next

        while temp is not self.head:
            if temp.data == target:
                return True
            temp = temp.next

        return False

    def get_element_and_prev_element_by_data(self, data):
        if self.isEmpty():
            return {"previous_element": None, "current_element": None}

        if self.head.data == data:
            return {"previous_element": None, "current_element": self.head}

        temp, prev = self.head.next, None
        while temp is not self.head and temp.data != data:
            prev = temp
            temp = temp.next

        if temp == self.head:
            return {"previous_element": None, "current_element": None}

        return {"previous_element": prev, "current_element": temp}

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
