from collections import defaultdict


def solution(dirs):
    answer = 0
    x, y = 5, 5
    memory = [[0 for _ in range(11)] for _ in range(11)]
    memory[x][y] = 1

    commands = {
        "U": lambda x, y: (x, y + 1),
        "D": lambda x, y: (x, y - 1),
        "R": lambda x, y: (x + 1, y),
        "L": lambda x, y: (x - 1, y),
    }

    condition = (lambda x, y: 0 <= x <= 10 and 0 <= y <= 10)
    for dir in dirs:
        tmp_x = x
        tmp_y = y
        x, y = commands[dir](x, y)
        if condition(x, y):
            memory[x][y] = 1
        else:
            x, y = tmp_x, tmp_y

        print(x, y)
        print(memory)

    answer = sum(cnt.count(1) for cnt in memory)

    return answer


# print(solution("ULURRDLLU"))
# print("hello"+''.capitalize()+"myname")
# t = bin(3)
# print(t)
# for i in t:
#     print(type(i))
#     break
# print(t.count('1'))


def is_pair(s):
    # 함수를 완성하세요
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w == "(" else x-1 if w == ")" else x
    return x == 0


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(is_pair("(hello)()"))
print(is_pair(")("))


def is_pair(s: str):
    return s.find("(") < s.find(")") and s.count("(") == s.count(")")


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(is_pair("(hello)()"))
print(is_pair(")("))
print(is_pair("() )( ()"))
