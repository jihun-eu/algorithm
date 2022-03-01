import enum
import sys

curr = list(map(int, sys.stdin.readline().split()))
timer = int(sys.stdin.readline())


def time_convert(curr):
    return curr[0] * 3600 + curr[1] * 60 + curr[2]


def time_seperator(timer):
    reg_t = [0] * 3

    for i, n in enumerate([3600, 60, 1]):
        reg_t[i] = timer // n
        timer %= n
        if i == 0:
            reg_t[i] %= 24
    return reg_t


print(' '.join(list(map(str, time_seperator(time_convert(curr) + timer)))))
