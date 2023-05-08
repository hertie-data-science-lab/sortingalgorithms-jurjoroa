# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 08:53:11 2023

@author: Hannah
"""

import math

def iterative_radix_sort(arr):
    """
    Sorts an array of integers using an iterative radix sort algorithm.
    :param arr: A list of integers to be sorted.
    :return: A sorted list of integers.
    """
    if not arr:
        return arr

    max_exp = math.floor(math.log10(max(arr))) + 1

    for exp in range(1, max_exp + 1):
        place_value = 10 ** (exp - 1)
        buckets = [[] for _ in range(10)]

        for num in arr:
            digit = (num // place_value) % 10
            buckets[digit].append(num)

        arr = [num for bucket in buckets for num in bucket]

    return arr

# Example usage
array = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", array)
sorted_array = iterative_radix_sort(array)
print("Sorted array:", sorted_array)

