
def rm_min(scores: list):
    scores.remove(min(scores))
    return sum(scores)


def main():
    score1 = [int(input()) for _ in range(4)]
    score2 = [int(input()) for _ in range(2)]

    print(rm_min(score1) + rm_min(score2))


if __name__ == "__main__":
    main()
