from math import sqrt


def main():
    diagonal, h_rate, w_rate = map(int, input().split())

    diagonal = diagonal ** 2

    x = sqrt(diagonal / (h_rate ** 2 + w_rate ** 2))
    height = h_rate * x
    width = w_rate * x

    print(int(height), int(width))


if __name__ == "__main__":
    main()
