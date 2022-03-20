
def main():
    arcs = sorted([int(input()) for _ in range(3)])
    if sum(arcs) != 180:
        return "Error"
    if all(map(lambda x: x == 60, arcs)):
        return "Equilateral"
    if any(map(lambda x: arcs.count(x) == 2, arcs)):
        return "Isosceles"
    return "Scalene"


if __name__ == "__main__":
    status = main()
    print(status)
