import sys


def main():
    row, col = map(int, sys.stdin.readline().rstrip().split())
    bread_shape = []
    for _ in range(row):
        code_line = sys.stdin.readline().rstrip()
        bread_shape.append(code_line[::-1])

    print(*bread_shape, sep="\n")


if __name__ == "__main__":
    main()
