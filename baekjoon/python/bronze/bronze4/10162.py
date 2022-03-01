import sys

btn = [300, 60, 10]

timer = int(sys.stdin.readline())


def min_count(timer):
    if timer % 10:
        return [-1]

    cnt = [0] * 3
    for i, t in enumerate(btn):
        cnt[i] = (timer // t)
        timer %= t

    return cnt


print(' '.join(list(map(str, min_count(timer)))))
