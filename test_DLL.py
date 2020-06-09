import unittest

from DataStructures import DoubleLinkedList

class TestDLL(unittest.TestCase):

    def test_empty(self):

        ll = DoubleLinkedList()
        self.assertEqual(len(ll), 0)

    def test_len_3(self):

        ll = DoubleLinkedList(range(3))
        self.assertEqual(len(ll), 3)

    def test_getitem(self):

        ll = DoubleLinkedList(range(3))
        self.assertEqual(ll[0], 0)
        self.assertEqual(ll[1], 1)
        self.assertEqual(ll[2], 2)

    def test_setitem(self):
        
        ll = DoubleLinkedList(range(3))
        ll[1] = 511
        self.assertEqual(ll[1], 511)

    def test_setitem_back(self):

        ll = DoubleLinkedList(range(3))
        ll[-1] = 511
        self.assertEqual(ll[-1], 511)

    def test_list_comprehension(self):

        ll = DoubleLinkedList(range(3))
        my_list = list(range(3))

        self.assertEqual(my_list, [x for x in ll])

    def test_append(self):

        ll = DoubleLinkedList(range(3))
        ll.append(3)
        
        self.assertEqual(ll[-1], 3)
        self.assertEqual(len(ll), 4)

    def test_append_to_empty(self):

        ll = DoubleLinkedList()
        ll.append(0)

        self.assertEqual(ll[0], 0)
        self.assertEqual(len(ll), 1)

    def test_pop(self):

        ll = DoubleLinkedList(range(3))

        self.assertEqual(ll.pop(), 2)
        self.assertEqual(len(ll), 2)

    def test_pop_from_index(self):

        ll = DoubleLinkedList(range(10))

        self.assertEqual(ll.pop(5), 5)
        self.assertEqual(len(ll), 9)

    def test_pop_from_front(self):

        ll = DoubleLinkedList(range(10))
        
        self.assertEqual(ll.pop(0), 0)
        self.assertEqual(ll[0], 1)
        self.assertEqual(len(ll), 9)

    def test_pop_from_back_index(self):

        ll = DoubleLinkedList(range(10))

        self.assertEqual(ll.pop(9), 9)
        self.assertEqual(len(ll), 9)
        self.assertEqual(ll[-1], 8)

    def test_insert_back(self):

        ll = DoubleLinkedList(range(10))

        ll.insert(10, 511)
        self.assertEqual(len(ll), 11)
        self.assertEqual(ll[-1], 511)

    def test_insert_middle(self):

        ll = DoubleLinkedList(range(10))

        ll.insert(5, 511)
        self.assertEqual(len(ll), 11)
        self.assertEqual(ll[5], 511)
        self.assertEqual(ll[4], 4)
        self.assertEqual(ll[6], 5)

    def test_insert_front(self):

        ll = DoubleLinkedList(range(10))

        ll.insert(0, 511)
        self.assertEqual(len(ll), 11)
        self.assertEqual(ll[0], 511)
        self.assertEqual(ll[1], 0)

    def test_pop_empty_exception(self):

        ll = DoubleLinkedList(range(3))

        for _ in range(3):
            ll.pop()
        with self.assertRaises(IndexError) as context:
            ll.pop()

    def test_pop_empty_exception2(self):

        ll = DoubleLinkedList(range(3))

        for _ in range(3):
            ll.pop(0)
        with self.assertRaises(IndexError) as context:
            ll.pop(0)

    def test_pop_out_of_range(self):

        ll = DoubleLinkedList(range(3))

        with self.assertRaises(IndexError) as context:
            ll.pop(10)

    def test_getitem_neg(self):

        ll = DoubleLinkedList(range(5))

        ll.insert(2, 511)

        self.assertEqual(ll[-3], 2)
        self.assertEqual(ll[-4], 511)
        self.assertEqual(ll[-5], 1)
        self.assertEqual(ll[-6], 0)

if __name__ == "__main__":
    unittest.main() 
