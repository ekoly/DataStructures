from DataStructures import LinkedList

class Stack(LinkedList):

    def push(self, val):
        self.append(val)

    def pop(self):
        return super().pop()
