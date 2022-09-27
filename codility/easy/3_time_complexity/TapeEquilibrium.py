'''
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7 
P = 2, difference = |4 − 9| = 5 
P = 3, difference = |6 − 7| = 1 
P = 4, difference = |10 − 3| = 7 
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
'''


import sys


def solution1(A):  # 38%
    min_diff = abs(A[0] - sum(A[1:]))
    for i in range(1, len(A)):
        tmp = abs(sum(A[:i+1]) - sum(A[i+1:]))
        min_diff = min(tmp, min_diff)

    return min_diff


def solution2(A):  # 84%
    first_part = 0
    second_part = sum(A)
    min_diff = sys.maxsize
    for i in range(len(A)):
        first_part += A[i]
        second_part -= A[i]
        min_diff = min(min_diff, abs(first_part - second_part))

    return min_diff


def solution(A):
    # write your code in Python 3.6
    left = 0
    right = sum(A)
    carry = None
    for i in range(1, len(A)):
        left += A[i]
        right -= A[i]
        tmp = abs(left - right)
        carry = min(carry, tmp)

    return carry


def solution(A):
    sum_of_part_one = 0
    sum_of_part_two = sum(A)
    min_difference = None

    for i in range(1, len(A)):
        sum_of_part_one += A[i-1]
        sum_of_part_two -= A[i-1]
        difference = abs(sum_of_part_one - sum_of_part_two)

        if min_difference == None:
            min_difference = difference
        else:
            min_difference = min(min_difference, difference)

    return min_difference
