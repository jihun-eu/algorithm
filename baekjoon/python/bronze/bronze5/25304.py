from operator import mul


def main():
    total_price = int(input())
    for _ in range(int(input())):
        total_price -= mul(*list(map(int, input().split())))
    return "Yes" if total_price == 0 else "No"


if __name__ == "__main__":
    print(main())
