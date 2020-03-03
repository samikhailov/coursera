n = [int(i) for i in input().split()]


def CountSort(n):
    tmp = [0 for i in range(max(n) + 1)]
    for i in range(len(n)):
        tmp[n[i]] += 1
    index = 0
    for counetr, i in enumerate(tmp):
        for j in range(i):
            n[index] = counetr
            index += 1
    return n


print(*CountSort(n))
