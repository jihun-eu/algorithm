import sys

radix, original = map(int, sys.stdin.readline().split())

print(f"{original - radix} {original}")
