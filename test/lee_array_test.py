#! /usr/local/bin
# -*- coding=UTF-8 -*-
# lee_array_test.py

import sys
sys.path.append("/Users/duzhiqiang/Code/leetcode/src")

import unittest
from lee_array import *

__author__ = "v-zhidu"


class TestArray(unittest.TestCase):

    # 532
    def test_find_pairs(self):
        list = [1, 3, 1, 4, 6]
        # k输入为负数时，应返回0
        k = -1
        self.assertEquals(find_pairs(list, k), 0, "k输入为负数时，应返回0")

        # k输入为0时，应返回list中重复的个数
        k = 0
        self.assertEquals(find_pairs(list, k), 1, "k输入为0时，应返回list中重复的个数")

        # k-diff
        k = 3
        self.assertEquals(find_pairs(list, k), 2, "k-diff")

    def test_find_max_consecutive_ones(self):
        list = [1, 1, 1, 0, 1, 1]

        self.assertEquals(find_max_consecutive_ones(list), 3)

    def test_find_poisoned_duration(self):

        # Line 11: IndexError: list index out of range
        list3 = []
        k = 1000
        self.assertEquals(find_poisoned_duration(list3, k), 0)

        # 判断持续时间为0的情况
        list = [1, 2]
        k = 0
        self.assertEquals(find_poisoned_duration(list, k), 0)

        # 第一种情况
        list1 = [1,2,3,4,5,6,7,8,9]
        k = 1
        self.assertEquals(find_poisoned_duration(list1, k), 9)

        # 第二种情况
        list2 = [1, 2]
        k = 2
        self.assertEquals(find_poisoned_duration(list2, k), 3)

    def test_find_disappeared_numbers(self):
        list = [4,3,2,7,8,2,3,1]
        self.assertEquals(find_disappeared_numbers(list), [5, 6])

    def test_find_duplicates(self):
        list = [4,3,2,7,8,2,3,1]
        self.assertEquals(find_duplicates(list), [2, 3])

    def test_find_third_max(self):
        list1 = [1, 2, 3]
        self.assertEquals(find_third_max(list1), 1)

        list1 = [1, 2]
        self.assertEquals(find_third_max(list1), 2)

        list1 = [2, 2, 3, 1]
        self.assertEquals(find_third_max(list1), 1)

        list1 = [1, 1, 2]
        self.assertEquals(find_third_max(list1), 2)

if __name__ == '__main__':
    unittest.main()
