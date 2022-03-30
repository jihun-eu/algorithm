def skill_difference(group1, group2):
    return abs(group1 - group2)


def main():
    members = list(map(int, input().split()))
    print(skill_difference(
        members[0] + members[3], members[1] + members[2]))


if __name__ == "__main__":
    main()
