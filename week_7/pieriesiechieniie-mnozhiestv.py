l1 = set([int(i) for i in input().split()])
l2 = set([int(i) for i in input().split()])

print(*sorted(l1 & l2))
