# -*- encoding=utf-8 -*-
"""

leetcode数组标签下的题目
https://leetcode.com/tag/array/

"""
from __future__ import unicode_literals


class LeetCodeArray(object):

    """
    Include all problems under array.
    """
    @staticmethod
    def find_pairs(nums, k):
        """
        532 -> 解法二
        """
        if k < 0:
            return 0

        count = 0
        d = {}
        for num in nums:
            if d.has_key(num):
                d[num] = d[num] + 1
            else:
                d[num] = 1
        if k == 0:
            for value in d.itervalues():
                if value > 1:
                    count = count + 1
        else:
            for num in d.iterkeys():
                if d.has_key(num + k):
                    count = count + 1

        return count

    @staticmethod
    def find_max_consecutive_ones(nums):
        """ summary of the function

        Args:
            nums: List[int]

        Returns:
            :rtype: int

        Raises:
        """
        count = 0
        result = 0
        for num in nums:
            if num == 1:
                count += 1
                result = max(count, result)
            else:
                count = 0

        return result

    @staticmethod
    def find_poisoned_duration(time_series, duration):
        """ Teemo Attacking

        Args:
            timeSeries: List[int]
            duration: int

        Returns:

        Raises:
        """
        result = duration * len(time_series)
        for i in range(1, len(time_series)):
            result -= max(0, duration - (time_series[i] - time_series[i - 1]))

        return result

    @staticmethod
    def find_disappeared_numbers(nums):
        """ summary of the function

        Args:
            nums: List[int]

        Returns:
            :rtype: List[int]

        Raises:
        """
        for i in enumerate(nums):
            index = abs(i[1]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        arr = []
        for i in enumerate(nums):
            if i[1] > 0:
                arr.append(i[0] + 1)

        return arr

    @staticmethod
    def find_duplicates(nums):
        """ summary of the function

        Args:

        Returns:

        Raises:
        """
        # Method 1
        # nums.sort()
        # res = []
        # for i in range(len(nums) - 1):
        #     if (nums[i] == nums[i + 1]):
        #         res.append(nums[i])

        # Method 2
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1

        return res

    @staticmethod
    def find_third_max(nums):
        """
        fs
        """
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)

        nums.sort()
        return nums[-3]


if __name__ == '__main__':
    nums = [1, 3, 1, 4, 5]
    k = 0
    print(LeetCodeArray.find_pairs_1(nums, k))
