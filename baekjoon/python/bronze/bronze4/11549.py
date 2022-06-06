def main():
    tea_type = int(input())
    contestants_answer = list(map(int, input().split()))

    print(contestants_answer.count(tea_type))


if __name__ == "__main__":
    main()
