import sys

row, col, seat = map(int, sys.stdin.readline().split())

n = int(seat / col)
m = seat % col

print(f"{n} {m}")
