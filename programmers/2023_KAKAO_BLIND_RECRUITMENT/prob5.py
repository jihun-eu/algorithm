memory = [[None for _ in range(51)] for _ in range(51)]
cache = {}


def update1(r, c, val):
    r, c = int(r), int(c)
    if isinstance(memory[r][c], tuple):
        cache[memory[r][c]] = val
    else:
        memory[r][c] = val


def update2(val1, val2):
    cache[val1] = val2


def merge(r1, c1, r2, c2):
    r1, c1, r2, c2 = map(int, [r1, c1, r2, c2])
    if memory[r1][c1]:
        if isinstance(memory[r1][c1], tuple):
            memory[r2][c2] = 
        cache[(r1, c1)] = memory[r1][c1]
    elif memory[r2][c2]:
        cache[(r1, c1)] = memory[r2][c2]
    else:
        cache[(r1, c1)] = ''
    memory[r2][c2] = (r1, c1)
    memory[r1][c1] = (r1, c1)


def unmerge(r, c):
    r, c = int(r), int(c)
    value = memory[r][c]
    if isinstance(value, tuple):
        memory[r][c] = cache[value]
    del cache[value]


def printing(r, c):
    r, c = int(r), int(c)
    return memory[r][c] if memory[r][c] else "EMPTY"


def solution(commands):
    answer = []
    for command in commands:
        command, args = (lambda x: (x[0], x[1:]))(command.split())
        if command == "UPDATE":
            if len(args) == 3:
                update1(*args)
            else:
                update2(*args)
        if command == "MERGE":
            merge(*args)
        if command == "UNMERGE":
            unmerge(*args)
        if command == "PRINT":
            answer.append(printing(*args))

    return answer


if __name__ == "__main__":
    # t = solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant",
    #               "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])
    # print(t)
    # for m in memory:
    #     print(m)
    # print(cache)
    # assert t == ["EMPTY", "group"]

