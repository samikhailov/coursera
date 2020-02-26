import sys

n = int(input())
l = [int(i) for i in input().split()]
x = int(input())

sim = abs(l[0] - x)
for i in l:
    if abs(i - x) < abs(i - sim):
        sim = i
    elif abs(i - x) == 0:
        print(i)
        sys.exit(0)
print(sim)
