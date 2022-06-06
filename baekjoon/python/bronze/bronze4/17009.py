def get_shooting_score():
    team_score = 0
    for score in [3, 2, 1]:
        team_score += (int(input()) * score)
    return team_score


def main():

    apple_team_score = get_shooting_score()
    banana_team_score = get_shooting_score()

    if apple_team_score < banana_team_score:
        print("B")
    elif apple_team_score > banana_team_score:
        print("A")
    else:
        print("T")


if __name__ == "__main__":
    main()
