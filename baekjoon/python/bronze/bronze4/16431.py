def main():
    point = [[0, 0], [0, 0], [0, 0]]
    for i in range(3):
        point[i][0], point[i][1] = map(int, input().split())

    bessie = max(abs(point[2][0] - point[0][0]),
                 abs(point[2][1] - point[0][1]))
    daisy = abs(point[2][0] - point[1][0]) + abs(point[2][1] - point[1][1])

    if bessie < daisy:
        print("bessie")
    elif bessie == daisy:
        print("tie")
    else:
        print("daisy")


if __name__ == "__main__":
    main()
