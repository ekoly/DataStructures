from DataStructures import Queue

class BSTNode:

    def __init__(self, obj, left=None, right=None):
        assert isinstance(left, BSTNode) or left is None
        assert isinstance(right, BSTNode) or right is None
        self.__val = obj
        self.__left = left
        self.__right = right

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, obj):
        self.__val = obj

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        assert isinstance(left, BSTNode) or left is None
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        assert isinstance(right, BSTNode) or right is None
        self.__right = right

class BinarySearchTree:

    def __init__(self, *args):
        assert len(args) <= 1
        self.__root = None
        if args:
            container = args[0]
            for x in container:
                self.insert(x)

    def insert(self, x):
        if not self.__root:
            self.__root = BSTNode(x)
            return

        node = self.__root
        while True:

            if x < node.val:
                if node.left is None:
                    node.left = BSTNode(x)
                    return
                else:
                    node = node.left

            elif node.val < x:
                if node.right is None:
                    node.right = BSTNode(x)
                    return
                else:
                    node = node.right

            else:
                return

    def remove(self, x):
        # TODO only works for root node
        if self.__root.val == x:
            if not self.__root.left and not self.__root.right:
                pass
            elif self.__root.left and not self.__root.right:
                self.__root = self.__root.left
            elif not self.__root.left and self.__root.right:
                self.__root = self.__root.right
            else:
                q = Queue([self.__root.left, self.__root.right])
                self.__root = None
                self.__absorbSubtree(q)
        else:
            parent = None
            node = self.__root
            while node is not None and node.val != x:
                parent = node
                if x < node.val:
                    node = node.left
                else:
                    node = node.right
            if node is None:
                raise ValueError("Value not in BST")
            if parent.left is node:
                if node.left is None and node.right is None:
                    parent.left = None
                elif node.left is None and node.right is not None:
                    parent.left = node.right
                elif node.left is not None and node.right is None:
                    parent.left = node.left
                else:
                    nodes = Queue([node.left, node.right])
                    parent.left = None
                    self.__absorbSubtree(nodes)
            else:
                if node.left is None and node.right is None:
                    parent.right = None
                elif node.left is None and node.right is not None:
                    parent.right = node.right
                elif node.left is not None and node.right is None:
                    parent.right = node.left
                else:
                    nodes = Queue([node.left, node.right])
                    parent.right = None
                    self.__absorbSubtree(nodes)

    def getMin(self):
        if self.__root is None:
            raise ValueError("Cannot get min of empty sequence")
        node = self.__root
        while node.left is not None:
            node = node.left
        return node.val

    def getMax(self):
        if self.__root is None:
            raise ValueError("Cannot get max of empty sequence")
        node = self.__root
        while node.right is not None:
            node = node.right
        return node.val

    def __iter__(self):
        self.__lineup = []
        if self.__root is None:
            return self
        node = self.__root
        while node is not None:
            self.__lineup.append(node)
            node = node.left
        return self

    def __next__(self):
        if not self.__lineup:
            raise StopIteration()
        node = self.__lineup.pop()
        obj = node.val
        if node.right:
            node = node.right
            while node is not None:
                self.__lineup.append(node)
                node = node.left
        return obj

    def __contains__(self, x):

        node = self.__root

        while node is not None:
            if x < node.val:
                node = node.left
            elif node.val < x:
                node = node.right
            else:
                return True

        return False

    def __absorbSubtree(self, q):

        while not q.isEmpty():
            node = q.pop()
            if node.left:
                q.push(node.left)
            if node.right:
                q.push(node.right)
            self.insert(node.val)
