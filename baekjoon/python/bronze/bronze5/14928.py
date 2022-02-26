import sys

num = sys.stdin.readline().strip('\n')
# num = "31231231545275482452"
std = 20000303


def mod(num, std):
    remainder = 0
    for i in range(len(num)):
        remainder = (remainder * 10 + int(num[i])) % std
        print(remainder, i)
    return remainder

# print(mod(num, 20000303))
# print(mod("31231231545275482452", 20000303))


print(int(num) % std)
