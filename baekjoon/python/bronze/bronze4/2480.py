import sys

prize = None
dice = list(map(int, sys.stdin.readline().split()))
for num in dice:
    counter = dice.count(num)
    if counter == 3:
        prize = 10000 + (num * 1000)
        break
    elif counter == 2:
        prize = 1000 + (num * 100)
        break
if not prize:
    prize = max(dice) * 100

print(prize)
