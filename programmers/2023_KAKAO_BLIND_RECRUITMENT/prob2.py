def func(cap: int, n: int, deliveries: list, pickups: list):
    cache = 0
    path_length = 0
    last_index = -1
    for i in range(n):
        cache += deliveries[i]
        if cap <= cache:
            path_length += (i+1) * (cache // cap)
            cache = cache % cap
            for i in range(i, -1, -1):
                if pickup_cache < cache:
                    pickup_cache += pickups[i]

        if deliveries[i]:
            last_index = i + 1
    if cache:
        path_length += last_index
    print(path_length)
    return path_length


def solution(cap: int, n: int, deliveries: list, pickups: list):

    answer = max(func(cap, n, deliveries), func(cap, n, pickups)) * 2
    print(answer)
    return answer
