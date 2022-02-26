import sys

rats_captured_first_day, rats_captured_second_day, rats_captured_both = map(
    int, sys.stdin.readline().split())

total_rats = int((rats_captured_first_day + 1) *
                 (rats_captured_second_day + 1) // (rats_captured_both + 1) - 1)

print(total_rats)
