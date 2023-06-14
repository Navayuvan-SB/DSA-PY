class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList:
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

    def insert_first(self, value):
        node = Node(value)

        if self.isEmpty():
            self.head = node
            return

        node.next = self.head
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
        current_element.next = node

    def insert_before(self, value, data):
        node = Node(value)

        if self.isEmpty():
            self.head = node
            return

        result = self.get_element_and_prev_element_by_data(data)
        prev_element = result["previous_element"]
        current_element = result["current_element"]

        if current_element is None:
            return

        prev_element.next = node
        node.next = current_element

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

        if prev_element is None:
            self.head = self.head.next
            return
        prev_element.next = current_element.next

    def delete_first(self):
        if self.isEmpty():
            return

        self.head = self.head.next

    def delete_last(self):
        if self.isEmpty():
            return

        prev, temp = None, self.head

        while temp.next is not None:
            prev = temp
            temp = temp.next

        prev.next = temp.next

    def get_element_by_data(self, data):
        if self.isEmpty():
            return None

        temp = self.head
        while temp and temp.data != data:
            temp = temp.next

        return temp

    def search(self, target):
        temp = self.head
        while temp is not None:
            if temp.data == target:
                return True
            temp = temp.next

        return False

    def get_element_and_prev_element_by_data(self, data):
        if self.isEmpty():
            return {"previous_element": None, "current_element": None}

        temp, prev = self.head, None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next

        return {"previous_element": prev, "current_element": temp}

    def display(self):
        if self.isEmpty():
            return print("list is empty")

        temp = self.head
        while temp is not None:
            print(temp.data, " -> ")
            temp = temp.next

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
