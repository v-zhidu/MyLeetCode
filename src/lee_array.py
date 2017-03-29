#! /usr/local/bin
# -*- coding=UTF-8 -*-
# lee_array.py

__author__ = "v-zhidu"


def find_pairs(nums, k):
    """ 532. K-diff Pairs in an Array

    Args:
        nums: List[int]
        k: int

    Returns:
        :rtype: int

    Raises:
    """

    if k < 0:
        return 0

    dict = {}
    s = 0
    for num in nums:
        if (dict.has_key(num)):
            dict[num] = dict[num] + 1
        else:
            dict[num] = 1

    if k == 0:
        for value in dict.itervalues():
            if value > 1:
                s = s + 1
    else:
        for key in dict.iterkeys():
            if dict.has_key(key + k):
                s = s + 1

    return s


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


def find_poisoned_duration(timeSeries, duration):
    """ Teemo Attacking

    Args:
        timeSeries: List[int]
        duration: int

    Returns:

    Raises:
    """
    result = duration * len(timeSeries)
    for i in range(1, len(timeSeries)):
        result -= max(0, duration - (timeSeries[i] - timeSeries[i - 1]))

    return result


def find_disappeared_numbers(nums):
    """ summary of the function

    Args:
        nums: List[int]

    Returns:
        :rtype: List[int]

    Raises:
    """
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]

    a = []
    for i in range(len(nums)):
        if nums[i] > 0:
            a.append(i + 1)

    return a


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
    for x in nums:
        if nums[abs(x) - 1] < 0:
            res.append(abs(x))
        else:
            nums[abs(x) - 1] *= -1

    return res


def find_third_max(nums):

    nums = list(set(nums))
    if len(nums) < 3:
        return max(nums)

    nums.sort()
    return nums[-3]


def main():
    pass


if __name__ == '__main__':
    main()
