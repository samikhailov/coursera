H = int(input())
A = int(input())
B = int(input())
S = 0
counter = 1
while True:
    S += A
    if S >= H:
        break
    S -= B
    counter += 1
print(counter)
