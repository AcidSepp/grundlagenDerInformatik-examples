from .list import *
import unittest


class TestStringMethods(unittest.TestCase):

    def test_equals(self):
        l1: IntList = IntList(None, None)
        l2: IntList = IntList(None, None)
        self.assertEqual(l1, l2)

    def test_equals2(self):
        l1: IntList = IntList(1, IntList(2, IntList(None, None)))
        l2: IntList = IntList(1, IntList(2, IntList(None, None)))
        self.assertEqual(l1, l2)

    def test_notEquals(self):
        l1: IntList = IntList(1, IntList(3, IntList(None, None)))
        l2: IntList = IntList(1, IntList(2, IntList(None, None)))
        self.assertNotEqual(l1, l2)

    def test_notEquals2(self):
        l1: IntList = IntList(1, IntList(None, None))
        l2: IntList = IntList(1, IntList(2, IntList(None, None)))
        self.assertNotEqual(l1, l2)

    def test_append(self):
        l1: IntList = IntList(1, IntList(None, None))
        l2: IntList = IntList(1, IntList(2, IntList(None, None)))
        l1.append(2)
        self.assertEqual(l1, l2)

    def test_insert(self):
        actual: IntList = IntList(1, IntList(3, IntList(4, IntList(None, None))))
        expected: IntList = IntList(1, IntList(2, IntList(3, IntList(4, IntList(None, None)))))
        self.assertEqual(expected, insert(actual, 2))

    def test_insert_first(self):
        actual: IntList = IntList(2, IntList(3, IntList(4, IntList(None, None))))
        expected: IntList = IntList(1, IntList(2, IntList(3, IntList(4, IntList(None, None)))))
        self.assertEqual(expected, insert(actual, 1))

    def test_insert_last(self):
        actual: IntList = IntList(1, IntList(2, IntList(3, IntList(None, None))))
        expected: IntList = IntList(1, IntList(2, IntList(3, IntList(4, IntList(None, None)))))
        self.assertEqual(expected, insert(actual, 4))

    def test_sort(self):
        actual: IntList = IntList(2, IntList(1, IntList(3, IntList(None, None))))
        expected: IntList = IntList(1, IntList(2, IntList(3, IntList(None, None))))
        self.assertEqual(expected, sort(actual))

    def test_sort_empty_list(self):
        actual: IntList = IntList(None, None)
        expected: IntList = IntList(None, None)
        self.assertEqual(expected, sort(actual))

    def test_concat(self):
        l1: IntList = IntList(1, IntList(2, IntList(None, None)))
        l2: IntList = IntList(3, IntList(4, IntList(None, None)))
        expected: IntList = IntList(1, IntList(2, IntList(3, IntList(4, IntList(None, None)))))
        self.assertEqual(expected, l1.concat(l2))



if __name__ == '__main__':
    unittest.main()
