#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Jorge Roa | Carmen Garro
"""

def bucket_sort_recurse(array, bucket_size=5, descending=False, recursion_limit=10, key=None):
    """
    Sorts an array using a recursive bucket sort algorithm.
    
    Args:
        array (list): The list of elements to be sorted.
        bucket_size (int, optional): The size of each bucket. Defaults to 5.
        descending (bool, optional): Set to True to sort the array in descending order.
        recursion_limit (int, optional): The maximum number of recursive calls before switching to a different sorting algorithm.
        key (function, optional): A function to specify the value to be used for sorting each element.
        
    Returns:
        list: A sorted version of the input array.
    """
    #Check if the array is empty
    if len(array) == 0:
        return []

    #Check if the array contains only strings
    if all(isinstance(x, str) for x in array):
        return sorted(array, reverse=descending, key=key)

    #Check if the array contains only numbers
    max_value = max(array)
    min_value = min(array)
    
    #Check if the array contains only identical elements
    if max_value == min_value:
        return array

    #Calculate the number of buckets
    range_size = max_value - min_value
    
    #Create empty buckets
    buckets = [[] for _ in range(bucket_size + 1)]
    
    #Add elements to the buckets
    for j in array:
        if key:
            j_value = key(j)
        else:
            j_value = j
        #Calculate the index of the bucket
        index_b = int((j_value - min_value) / range_size * bucket_size)
        # Add j to corresponding bucket
        buckets[index_b].append(j)

    #Sort the elements of each bucket recursively, or switch to a different sorting algorithm after a certain number of recursive calls
    sorted_buckets = []
    if recursion_limit > 0:
        for i in range(bucket_size + 1):
            if len(buckets[i]) > 0:
                sorted_bucket = bucket_sort_recurse(buckets[i], bucket_size, descending, recursion_limit - 1, key)
                sorted_buckets.extend(sorted_bucket)
    else:
        for i in range(bucket_size + 1):
            if len(buckets[i]) > 0:
                if key:
                    sorted_bucket = sorted(buckets[i], reverse=descending, key=key)
                else:
                    sorted_bucket = sorted(buckets[i], reverse=descending)
                sorted_buckets.extend(sorted_bucket)

    #Return the sorted buckets
    return sorted_buckets[::-1] if descending else sorted_buckets


#Example usage
array = ['apple', 'banana', 'orange', 'grape', 'pear']
sorted_array = bucket_sort_recurse(array)
print(sorted_array)

#Sort the array in descending order
array = [5, 2, 9, 1, 5, 3, 7, 0, 10, 6]
sorted_array = bucket_sort_recurse(array, bucket_size=10, descending=True, recursion_limit=5)
print(sorted_array)

#Sort an empty array
array = []
sorted_array = bucket_sort_recurse(array)
print(sorted_array)

