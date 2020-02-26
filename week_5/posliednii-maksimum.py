n = [int(i) for i in input().split()]
max_num = n[0]

for counter, i in enumerate(n):
    if max_num <= i:
        max_num = i
        max_index = counter
print(max_num, max_index)
