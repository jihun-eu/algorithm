import sys


def main():
    secret_code = []
    while True:
        code_line = sys.stdin.readline().rstrip()
        if code_line == "END":
            break

        secret_code.append(code_line[::-1])

    print(*secret_code, sep="\n")


if __name__ == "__main__":
    main()
