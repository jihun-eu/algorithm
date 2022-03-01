import sys

num = list(map(int, sys.stdin.readline().split()))
print(' '.join(list(map(str, sorted(num)))))


def bubble_sort():
    for i in range(3):
        for j in range(i+1, 3):
            if num[j] < num[i]:
                num[i], num[j] = num[j], num[i]


bubble_sort()
