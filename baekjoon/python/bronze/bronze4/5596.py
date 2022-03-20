def main():
    scores = [sum(map(int, input().split())) for _ in range(2)]
    return max(scores)


if __name__ == "__main__":
    max_scores = main()
    print(max_scores)
