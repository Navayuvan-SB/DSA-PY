class Queue:
    def __init__(self, size=5):
        self.array = []
        self.size = size

    def enqueue(self, element):
        if self.isFull():
            raise Exception("queue overflow")
        self.array.append(element)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("queue underflow")
        return self.array.pop(0)

    def isFull(self):
        return len(self.array) == self.size

    def isEmpty(self):
        return len(self.array) == 0

    def display(self):
        print(self.array)

    def get_queue(self):
        return self.array
