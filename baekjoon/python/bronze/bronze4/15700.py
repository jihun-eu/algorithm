def main():
    n, m = map(int, input().split())

    max_res = max(n, m)
    min_res = min(n, m)

    print(((max_res // 2) * min_res) + (max_res % 2) * (min_res // 2))


if __name__ == "__main__":
    main()
