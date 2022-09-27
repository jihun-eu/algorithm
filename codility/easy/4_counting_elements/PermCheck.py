# A non-empty array A consisting of N integers is given.

# A permutation is a sequence containing each element from 1 to N once, and only once.

# For example, array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# is a permutation, but array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# is not a permutation, because value 2 is missing.

# The goal is to check whether array A is a permutation.

# Write a function:

# def solution(A)

# that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# the function should return 1.

# Given array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# the function should return 0.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A: list):
    # write your code in Python 3.6

    max_value = max(A)
    prefix_sum = max_value * (max_value + 1) // 2

    if len(A) != max_value:
        return 0
    if prefix_sum != sum(A):
        return 0

    operated = [0] * (max_value + 1)
    for element in A:
        if operated[element] == 0:
            operated[element] += 1
            prefix_sum -= element
    if prefix_sum != 0:
        return 0
    return 1
