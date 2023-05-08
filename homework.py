#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@authors: Jorge Roa | Carmen Garro
"""
from bucket_final import bucket_sort_recurse


"""
This code defines a main function that tests the bucket_sort_recurse function with different input arrays:
    -Integers in ascending order.
    -Integers in descending order.
    -Float numbers.
    -Strings.
    -Strings sorted by length using a custom key function.
    -A mix of positive and negative integers.
"""


def main():
    # Test with integers in ascending order
    test_array1 = [37, 45, 29, 8, 12, 88, 53, 4, 23, 67]
    sorted_array1 = bucket_sort_recurse(test_array1)
    print("Sorted integers in ascending order:", sorted_array1)

    # Test with integers in descending order
    sorted_array2 = bucket_sort_recurse(test_array1, descending=True)
    print("Sorted integers in descending order:", sorted_array2)

    # Test with float numbers
    test_array3 = [3.7, 4.5, 2.9, 0.8, 1.2, 8.8, 5.3, 0.4, 2.3, 6.7]
    sorted_array3 = bucket_sort_recurse(test_array3)
    print("Sorted float numbers:", sorted_array3)

    # Test with strings
    test_array4 = ["Alejandro", "Eduardo", "Diana", "Maria", "Ana", "Luis", "Jorge", "Carmen", "Javier"]
    sorted_array4 = bucket_sort_recurse(test_array4)
    print("Sorted strings:", sorted_array4)

    # Test with a custom key function (sorting by length)
    test_array5 = ["Alejandro", "Eduardo", "Diana", "Maria", "Ana", "Luis", "Jorge", "Carmen", "Javier"]
    sorted_array5 = bucket_sort_recurse(test_array5, key=len)
    print("Sorted strings by length:", sorted_array5)

    # Test with a mix of positive and negative integers
    test_array6 = [-5, 12, 0, -3, 8, -11, 20, -8, 15, -2]
    sorted_array6 = bucket_sort_recurse(test_array6)
    print("Sorted mix of positive and negative integers:", sorted_array6)

if __name__ == "__main__":
    main()