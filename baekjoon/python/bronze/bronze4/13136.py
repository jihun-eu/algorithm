from math import ceil


def main():
    r, c, n = map(int, input().split())

    print(ceil(r/n) * ceil(c/n))


if __name__ == "__main__":
    main()
