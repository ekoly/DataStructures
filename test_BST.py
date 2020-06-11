import unittest

from DataStructures import BinarySearchTree

class test_BST(unittest.TestCase):

    def test_getmin(self):
        b = BinarySearchTree([x for x in range(100)])
        self.assertEqual(b.getMin(), 0)

    def test_getmax(self):
        b = BinarySearchTree([x for x in range(100)])
        self.assertEqual(b.getMax(), 99)

    def test_contains(self):
        b = BinarySearchTree()
        b.insert(5)
        b.insert(3)
        b.insert(7)
        self.assertTrue(3 in b)

    def test_contains2(self):
        b = BinarySearchTree()
        b.insert(5)
        b.insert(3)
        b.insert(7)
        self.assertTrue(5 in b)

    def test_contains3(self):
        b = BinarySearchTree()
        b.insert(5)
        b.insert(3)
        b.insert(7)
        self.assertTrue(8 not in b)

    def test_list_comprehension(self):
        b = BinarySearchTree()
        b.insert(5)
        b.insert(3)
        b.insert(7)
        self.assertEqual([x for x in b], [3, 5, 7])

    def test_remove_root(self):
        b = BinarySearchTree([64, 32, 96, 16, 48, 80, 112])
        b.remove(64)
        self.assertTrue(64 not in b)
        self.assertTrue(32 in b)
        self.assertTrue(96 in b)
        self.assertTrue(112 in b)

    def test_remove_node(self):
        b = BinarySearchTree([64, 32, 96, 16, 48, 80, 112])
        b.remove(32)
        self.assertTrue(64 in b)
        self.assertTrue(32 not in b)
        self.assertTrue(16 in b)
        self.assertTrue(48 in b)
        self.assertTrue(96 in b)
        self.assertTrue(112 in b)

if __name__ == "__main__":
    unittest.main()
