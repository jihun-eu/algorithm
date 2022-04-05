def main():
    a, b, c = map(int, input().split())
    print(int(max((a*b)/c, (a/b)*c)))


if __name__ == "__main__":
    main()
