import sys

cake_num = [0] * 2

for i in range(2):
    cake_num[i] = tuple(map(int, sys.stdin.readline().split()))

print(cake_num[1][0] - cake_num[0][2], cake_num[1][1] //
      cake_num[0][1], cake_num[1][2] - cake_num[0][0])

# a 🍰 b = (a.z + b.x, a.y × b.y, a.x + b.z)
