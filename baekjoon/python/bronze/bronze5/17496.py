import sys

summer, growth, space, price = map(int, sys.stdin.readline().split())

print((summer - 1) // growth * space * price)
