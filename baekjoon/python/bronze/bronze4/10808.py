

import sys


CHAR_DEVISOR = 97


def main():

    tmp = [0]*26

    voca = sys.stdin.readline().rstrip()

    for v in voca:
        tmp[ord(v) - CHAR_DEVISOR] += 1

    print(*tmp, sep=" ")


if __name__ == "__main__":
    main()
    # print(ord('z'))
