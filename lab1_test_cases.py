import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        self.assertEqual(max_list_iter([]), None)  # checks for an empty list passing into function, returns None
        self.assertEqual(max_list_iter([2,5,6,8]),8)  # returns max value in a given list
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])  # returns reversal of a given list
        self.assertEqual(reverse_rec([1]),[1])
        self.assertEqual(reverse_rec([]), [])  # checks for empty list passing into function, returns empty list
        intlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(intlist)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4)  # returns index of target value
        self.assertEqual(bin_search(6, low, high, list_val), None)  # checks if a target value exists in a given list, returns None
        list2_val = [13]
        high2 = len(list2_val)-1
        self.assertEqual(bin_search(13, low, high2, list2_val), 0)
        list3_val = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(2, low, high, list3_val)

if __name__ == "__main__":
        unittest.main()

    
