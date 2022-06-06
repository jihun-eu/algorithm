import sys


def main():

    accounts = sum(map(int, sys.stdin.readline().rstrip().split()))

    chicken_price = int(sys.stdin.readline().rstrip()) * 2

    if accounts < chicken_price:
        print(accounts)
    else:
        print(accounts - chicken_price)


if __name__ == "__main__":
    main()
