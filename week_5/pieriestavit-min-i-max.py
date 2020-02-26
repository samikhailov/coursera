l = [int(i) for i in input().split()]
index_min = l.index(min(l))
index_max = l.index(max(l))
l[index_min], l[index_max] = max(l), min(l)
print(*l)
