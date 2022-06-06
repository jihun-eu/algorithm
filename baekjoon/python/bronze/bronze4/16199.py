
def age_diff(standard, birth):
    diff = [(s - b) for s, b in zip(standard, birth)]

    if diff[1] < 0:
        return (diff[0] - 1, diff[0] + 1, diff[0])
    elif diff[1] == 0 and diff[2] < 0:
        return (diff[0] - 1, diff[0] + 1, diff[0])
    else:
        return (diff[0], diff[0] + 1, diff[0])


def main():
    birth = list(map(int, input().split()))
    standard_date = list(map(int, input().split()))

    for age in age_diff(standard_date, birth):
        print(age)


if __name__ == "__main__":
    main()
