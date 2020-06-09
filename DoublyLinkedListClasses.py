class ListNode:

    def __init__(self, obj, next_node=None, prev_node=None):
        assert isinstance(next_node, ListNode) or next_node is None
        assert isinstance(prev_node, ListNode) or prev_node is None
        self.__val = obj
        self.__next = next_node
        self.__prev = prev_node

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, obj):
        self.__val = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
        assert isinstance(next_node, ListNode) or next_node is None
        self.__next = next_node

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev_node):
        assert isinstance(prev_node, ListNode) or prev_node is None
        self.__prev = prev_node

class DoubleLinkedList:

    def __init__(self, *args):
        assert len(args) <= 1
        if args:
            iterable = args[0]
        else:
            iterable = []

        self.__head = None
        self.__tail = None

        for obj in iterable:
            self.append(obj)

    def append(self, obj):

        if self.__head is None:
            self.__head = self.__tail = ListNode(obj)

        else:
            self.__tail.next = ListNode(obj, prev_node=self.__tail)
            self.__tail = self.__tail.next

    def insert(self, index, obj):

        if self.__head is None:
            self.__head = self.__tail = ListNode(obj)

        elif index == 0:
            self.__head.prev = ListNode(obj, next_node=self.__head)
            self.__head = self.__head.prev

        else:
            if index >= 0:
                node = self.__head
                for _ in range(index):
                    if node is None:
                        break
                    node = node.next
                if node is None:
                    self.__tail.next = ListNode(obj, prev_node=self.__tail)
                    self.__tail = self.__tail.next
                    return

            else:
                node = self.__tail
                for _ in range(-index - 1):
                    if node is None:
                        break
                    node = node.prev
                if node is None:
                    self.__head.prev = ListNode(obj, next_node=self.__head)
                    self.__head = self.__head.prev
                    return

            if node.prev is None: # changing head
                self.__head.prev = ListNode(obj, next_node=self.__head)
                self.__head = self.__head.prev

            else:
                node.prev.next = ListNode(obj, next_node=node, prev_node=node.prev)
                node.prev = node.prev.next

    def pop(self, *args):

        assert len(args) <= 1

        if self.__head is None:
            raise IndexError("Cannot pop from empty list")

        if args:
            index = args[0]
            node = self.__get_node(index)
        else:
            node = self.__tail

        obj = node.val
        if node is self.__head and node is self.__tail:
            self.__head = self.__tail = None
        elif node is self.__head:
            self.__head.next.prev = None
            self.__head = self.__head.next
        elif node is self.__tail:
            self.__tail.prev.next = None
            self.__tail = self.__tail.prev
        else:
            node.prev.next, node.next.prev = node.next, node.prev

        return obj

    def __get_node(self, index):

        assert type(index) == int

        if self.__head is None:
            raise IndexError("Cannot access item in empty list")

        if index >= 0:
            node = self.__head
            for _ in range(index):
                if node.next is None:
                    raise IndexError("index out of range")
                node = node.next

        else:
            node = self.__tail
            for _ in range(-index - 1):
                if node.prev is None:
                    raise IndexError("index out of range")
                node = node.prev

        return node

    def __getitem__(self, index):
        return self.__get_node(index).val

    def __setitem__(self, index, obj):
        self.__get_node(index).val = obj

    def __delitem__(self, index):
        self.pop(index)

    def __repr__(self):
        return "DoubleLinkedList([" + ", ".join([str(x) for x in self]) + "])"

    def __iter__(self):
        self.__curr = self.__head
        return self

    def __next__(self):
        if self.__curr is None:
            raise StopIteration()
        obj = self.__curr.val
        self.__curr = self.__curr.next
        return obj

    def __len__(self):
        counter = 0
        node = self.__head
        while node is not None:
            node = node.next
            counter += 1
        return counter
