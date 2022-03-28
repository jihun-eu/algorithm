def main():
    s, t, d = map(int, input().split())

    time = d // (s * 2)
    print(t * time)


if __name__ == "__main__":
    main()
