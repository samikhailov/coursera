n = [int(i) for i in input().split()]


def sort(n):
    len_n = len(n)
    for i in range(len_n):
        for j in range(len_n - 1 - i):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
    return n


print(*sort(n))
