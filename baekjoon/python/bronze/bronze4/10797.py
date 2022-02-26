import sys

current_date = int(sys.stdin.readline())
car_lice_plates = list(map(int, sys.stdin.readline().split()))

print(car_lice_plates.count(current_date))
