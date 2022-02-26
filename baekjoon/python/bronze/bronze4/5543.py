import sys

menu = [0] * 5

for i in range(len(menu)):
    menu[i] = int(sys.stdin.readline())

print(min(menu[:3]) + min(menu[3:]) - 50)
