from math import ceil


def main():
    cnt = int(input())
    result = (cnt // 2 + 1) * (ceil(cnt / 2) + 1)
    print(result)


if __name__ == "__main__":
    main()
