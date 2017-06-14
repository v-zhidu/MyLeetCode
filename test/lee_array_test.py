# -*- encoding=utf-8 -*-
"""
lee_array_test.py
"""


from __future__ import unicode_literals

import unittest

from src import LeetCodeArray


class TestArray(unittest.TestCase):
    """
    test
    """

    def test_find_pairs(self):
        """
        test1
        """
        arr = [1, 3, 1, 4, 5]
        # k输入为负数时，应返回0
        k = -1
        self.assertEquals(LeetCodeArray.find_pairs(arr, k), 0, "k输入为负数时，应返回0")

        # k输入为0时，应返回arr中重复的个数
        k = 0
        self.assertEquals(LeetCodeArray.find_pairs(
            arr, k), 1, "k输入为0时，应返回arr中重复的个数")
        # k-diff
        k = 3
        self.assertEquals(LeetCodeArray.find_pairs(arr, k), 1, "k-diff")

    def test_find_max_consecutive_ones(self):
        """
        test
        """
        arr = [1, 1, 1, 0, 1, 1]

        self.assertEquals(LeetCodeArray.find_max_consecutive_ones(arr), 3)

    def test_find_poisoned_duration(self):
        """
        arrne 11: IndexError: arr index out of range
        """
        arr3 = []
        k = 1000
        self.assertEquals(LeetCodeArray.find_poisoned_duration(arr3, k), 0)

        # 判断持续时间为0的情况
        """
        arrne 11: IndexError: arr index out of range
        """
        arr = [1, 2]
        k = 0
        self.assertEquals(LeetCodeArray.find_poisoned_duration(arr, k), 0)

        # 第一种情况
        arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        k = 1
        self.assertEquals(LeetCodeArray.find_poisoned_duration(arr1, k), 9)

        # 第二种情况
        arr2 = [1, 2]
        k = 2
        self.assertEquals(LeetCodeArray.find_poisoned_duration(arr2, k), 3)

    def test_find_disappeared_numbers(self):
        """
        arrne 11: IndexError: arr index out of range
        """
        arr = [4, 3, 2, 7, 8, 2, 3, 1]
        self.assertEquals(LeetCodeArray.find_disappeared_numbers(arr), [5, 6])

    def test_find_duparrcates(self):
        """
        test
        """
        arr = [4, 3, 2, 7, 8, 2, 3, 1]
        self.assertEquals(LeetCodeArray.find_duplicates(arr), [2, 3])

    def test_find_third_max(self):
        """
        test
        """
        arr = [1, 2, 3]
        self.assertEquals(LeetCodeArray.find_third_max(arr), 1)

        arr = [1, 2]
        self.assertEquals(LeetCodeArray.find_third_max(arr), 2)

        arr = [2, 2, 3, 1]
        self.assertEquals(LeetCodeArray.find_third_max(arr), 1)

        arr = [1, 1, 2]
        self.assertEquals(LeetCodeArray.find_third_max(arr), 2)


if __name__ == '__main__':
    unittest.main()
