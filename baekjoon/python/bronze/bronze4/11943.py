def main():
    first_bucket = list(map(int, input().split()))
    second_bucket = list(map(int, input().split()))

    print(min((first_bucket[0] + second_bucket[1]),
          (first_bucket[1] + second_bucket[0])))


if __name__ == "__main__":
    main()
