def choose_num(n):
    num = n % 8
    if num == 0:
        return 2
    if num > 5:
        return 10 - num
    return num


def main():
    n = int(input())
    print(choose_num(n))


if __name__ == "__main__":
    main()
