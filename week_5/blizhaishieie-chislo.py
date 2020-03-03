n = int(input())
l = [int(i) for i in input().split()[:n]]
x = int(input())

min_num = l[0]
for i in l:
    if abs(x - i) < abs(x - min_num):
        min_num = i
print(min_num)
