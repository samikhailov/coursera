n = [int(i) for i in input().split()]

min_num = 1001
for i in n:
    if i > 0 and i < min_num:
        min_num = i
print(min_num)
