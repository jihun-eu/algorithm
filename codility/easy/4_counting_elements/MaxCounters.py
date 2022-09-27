# You are given N counters, initially set to 0, and you have two possible operations on them:

# increase(X) − counter X is increased by 1,
# max counter − all counters are set to the maximum value of any counter.
# A non-empty array A of M integers is given. This array represents consecutive operations:

# if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
# if A[K] = N + 1 then operation K is max counter.
# For example, given integer N = 5 and array A such that:

#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the values of the counters after each consecutive operation will be:

#     (0, 0, 1, 0, 0)
#     (0, 0, 1, 1, 0)
#     (0, 0, 1, 2, 0)
#     (2, 2, 2, 2, 2)
#     (3, 2, 2, 2, 2)
#     (3, 2, 2, 3, 2)
#     (3, 2, 2, 4, 2)
# The goal is to calculate the value of every counter after all operations.

# Write a function:

# def solution(N, A)

# that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

# Result array should be returned as an array of integers.

# For example, given:

#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the function should return [3, 2, 2, 4, 2], as explained above.

# Write an efficient algorithm for the following assumptions:

# N and M are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..N + 1].
# Copyright 2009–2022 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N: int, A: list):  # % 66 timeout
    # write your code in Python 3.6
    max_counter = N + 1
    memory = [-1] + [0] * N
    max_value = 0
    for i in range(len(A)):
        if A[i] == max_counter:
            max_value = max(memory)
            for j in range(1, max_counter):
                memory[j] = max_value
            max_value = 0
        else:
            memory[A[i]] += 1
    memory.pop(0)
    return memory

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N, A):  # % 100
    # write your code in Python 3.6
    counters = [0] * N
    max_counter = N + 1

    cache = 0
    current_max = 0
    for counter in A:
        counter_index = counter - 1
        if counter < max_counter:
            if counters[counter_index] < cache:
                counters[counter_index] = 1 + cache
            else:
                counters[counter_index] += 1
            if current_max < counters[counter_index]:
                current_max = counters[counter_index]
        else:
            cache = current_max

    for counter in range(N):
        if counters[counter] < cache:
            counters[counter] = cache

    return counters
