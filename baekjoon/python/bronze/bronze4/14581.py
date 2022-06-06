

import sys


def main():

    hong_id = ":"+sys.stdin.readline().rstrip()+":"

    for i in range(3):
        emoji = [":fan:"]*3
        if i == 1:
            emoji[1] = hong_id
        print(*emoji, sep="")


if __name__ == "__main__":
    main()
