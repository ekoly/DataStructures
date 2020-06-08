class ListNode:

    def __init__(self, val, next_node=None):
        assert isinstance(next_node, ListNode) or next_node is None

        self.__val = val
        self.__next = next_node

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val):
        self.__val = val

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
        assert isinstance(next_node, ListNode) or next_node is None
        self.__next = next_node

class LinkedList:

    def __init__(self, *iterable):
        assert len(iterable) <= 1

        self.__head = None
        self.__tail = None

        if iterable:
            iterable = iterable[0]
            for item in iterable:
                self.append(item)

    def insert(self, index, obj):

        if self.__head is None:
            self.__head = self.__tail = ListNode(obj)
            return

        prev = None
        node = self.__head

        for _ in range(index):
            prev = node
            node = node.next
            if node is None:
                break

        # inserting at head?
        if prev is None:
            self.__head = ListNode(obj, next_node=self.__head)

        # inserting at tail?
        elif node is None:
            self.__tail.next = ListNode(obj)
            self.__tail = self.__tail.next
        
        # inserting in middle
        else:
            prev.next  = ListNode(obj, next_node=node)

    def append(self, obj):
        """
            Push an obj at the end.
        """

        if self.__head is None:
            self.__head = self.__tail = ListNode(obj)

        else:
            self.__tail.next = ListNode(obj)
            self.__tail = self.__tail.next

    def pop(self, *index):
        assert len(index) <= 1

        if self.__head is None:
            raise IndexError("Cannot pop from empty list")

        if index:
            index = index[0]
            assert type(index) is int
            
            if index == 0:
                obj = self.__head.val
                if self.__head is self.__tail:
                    self.__tail = self.__tail.next
                self.__head = self.__head.next
                return obj

            prev = None
            node = self.__head
            for _ in range(index):
                if node.next is None:
                    raise IndexError("Index out of range")
                prev = node
                node = node.next

            obj = node.val

            if node is self.__tail:
                self.__tail = prev

            prev.next = node.next

        # no index given: pop from tail
        elif self.__head is self.__tail:
            obj = self.__tail.val
            self.__head = self.__tail = None

        else:
            prev = self.__head
            while prev.next is not self.__tail:
                prev = prev.next
            obj = self.__tail.val
            self.__tail = prev
            self.__tail.next = None

        return obj

    def __getitem__(self, index):
        assert type(index) is int

        if index < 0:
            index = len(self) + index
            if index < 0:
                raise IndexError("Index out of range")

        if self.__head is None:
            raise IndexError("Cannot access item in empty list")

        node = self.__head
        for _ in range(index):
           node = node.next
           if node is None:
               raise IndexError("Index out of range")

        return node.val

    def __setitem__(self, index, new_val):
        assert type(index) is int

        if index < 0:
            index = len(self) + index
            if index < 0:
                raise IndexError("Index out of range")

        if self.__head is None:
            raise IndexError("Cannot access item in empty list")

        node = self.__head
        for _ in range(index):
            node = node.next
            if node is None:
                raise IndexError("Index out of range")

        node.val = new_val

    def __iter__(self):
        self.__curr = self.__head
        return self

    def __next__(self):
        if self.__curr is None:
            raise StopIteration()
        obj = self.__curr.val
        self.__curr = self.__curr.next
        return obj

    def __repr__(self):
        return "LinkedList([" + ", ".join([str(x) for x in self]) + "])"

    def __str__(self):
        return "LinkedList([" + ", ".join([str(x) for x in self]) + "])"

    def __len__(self):
        counter = 0
        node = self.__head
        while node is not None:
            node = node.next
            counter += 1
        return counter
