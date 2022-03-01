from math import ceil
import sys

homework = [0] * 5

for i in range(5):
    homework[i] = int(sys.stdin.readline())

print(homework[0] - max(ceil(homework[1] / homework[3]),
      ceil(homework[2] / homework[4])))
