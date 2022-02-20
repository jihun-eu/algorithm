import sys


def get_two_int():
    return map(lambda x: int(x), sys.stdin.readline().split())


stations, passengers = get_two_int()
for _ in range(stations):
    get_two_int()

print("비와이")
