def main():
    n, w, h, l = map(int, input().split())
    print(min(n, (w // l) * (h // l)))


if __name__ == "__main__":
    main()
