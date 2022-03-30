def seperate_member(n, m):
    if m < 3:
        return "NEWBIE!"

    if m <= n:
        return "OLDBIE!"

    return "TLE!"


def main():
    n, m = map(int, input().split())
    print(seperate_member(n, m))


if __name__ == "__main__":
    main()
