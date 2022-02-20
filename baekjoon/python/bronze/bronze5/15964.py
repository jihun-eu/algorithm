import sys

num1, num2 = map(int, sys.stdin.readline().split())


def operator(x, y): return (x + y) * (x - y)


print(operator(num1, num2))
