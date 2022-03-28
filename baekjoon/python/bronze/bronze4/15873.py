
def calculate(num):
    if num[1] == "0":
        return 10 + int(num[2:])
    else:
        return int(num[0]) + int(num[1:])


def main():
    num = input()
    print(calculate(num))


if __name__ == "__main__":
    main()
