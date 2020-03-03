def sortirovka(l):
    return sorted(l)


if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    print(*sortirovka(l[:n]))
