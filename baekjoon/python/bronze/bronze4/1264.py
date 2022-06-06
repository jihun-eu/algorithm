import sys


def main():
    en_string = []
    while True:
        en_line = sys.stdin.readline().rstrip()
        if en_line == "#":
            break
        counter = 0
        for c in en_line.lower():
            if c in ['a', 'e', 'i', 'o', 'u']:
                counter += 1
        en_string.append(counter)

    print(*en_string, sep="\n")


if __name__ == "__main__":
    main()
