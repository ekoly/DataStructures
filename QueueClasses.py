from DataStructures import DoubleLinkedList


class Queue(DoubleLinkedList):

    def __init__(self, *args):
        super().__init__(*args)

    def push(self, val):
        self.append(val)

    def pop(self):
        return super().pop(0)

    def peek(self):
        return self[0]

class Deque(DoubleLinkedList):

    def pushFront(self, val):
        self.insert(0, val)

    def pushBack(self, val):
        self.append(val)

    def popFront(self):
        return super().pop(0)

    def popBack(self):
        return super().pop()

    def peekFront(self):
        return self[0]

    def peekBack(self):
        return self[-1]
