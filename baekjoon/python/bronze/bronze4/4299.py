def main():
    score_sum, score_sub = map(int, input().split())
    a = (score_sum + score_sub) / 2
    b = (score_sum - score_sub) / 2
    if a - int(a) or b - int(b):
        print(-1)
    elif a < 0 or b < 0:
        print(-1)
    else:
        print(int(a), int(b))


if __name__ == "__main__":
    main()
