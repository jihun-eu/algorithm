def cal_round(d1, d2):
    return 2 * ((3.141592 * d2) + d1)


def main():
    d1 = int(input())
    d2 = int(input())
    print(cal_round(d1, d2))


if __name__ == "__main__":
    main()
