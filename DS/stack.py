class Stack:
    def __init__(self, size=5):
        self.array = []
        self.size = size

    def push(self, element):
        if self.isFull():
            raise Exception("stack overflow")

        self.array.append(element)

    def pop(self):
        if self.isEmpty():
            raise Exception("stack underflow")

        return self.array.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("stack underflow")
        return self.array[-1]

    def isEmpty(self):
        return len(self.array) == 0

    def isFull(self):
        return len(self.array) == self.size

    def display(self):
        print(self.array)

    def get_stack(self):
        return self.array
