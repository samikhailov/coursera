n = [int(i) for i in input().split()]

for i in range(len(n) - 1):
    if n[i + 1] > n[i]:
        print(n[i + 1])
