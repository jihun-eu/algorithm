import sys

step = 5
dist = int(sys.stdin.readline())

total_time = int(dist / step) + 1 if dist % step else int(dist / step)

print(total_time)
