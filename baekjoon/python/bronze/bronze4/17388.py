def warn_univ(univ: list):

    univs = ["Soongsil", "Korea", "Hanyang"]

    if sum(univ) >= 100:
        return "OK"

    to_warn = univs[univ.index(min(univ))]
    return to_warn


def main():
    univ = list(map(int, input().split()))
    target = warn_univ(univ)
    print(target)


if __name__ == "__main__":
    main()
