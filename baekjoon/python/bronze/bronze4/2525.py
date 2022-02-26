import sys

current_time = list(map(int, sys.stdin.readline().split()))
required_time = int(sys.stdin.readline())

current_time[1] += required_time
current_time[0] += current_time[1] // 60
current_time[0] %= 24
current_time[1] %= 60

print(f"{current_time[0]} {current_time[1]}")
