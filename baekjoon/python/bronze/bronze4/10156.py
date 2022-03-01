import sys

price, num, budget = map(int, sys.stdin.readline().split())

allowance = price * num - budget
print(allowance if allowance > 0 else 0)
