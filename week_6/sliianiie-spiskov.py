def merge(a, b):
    len_a = len(a)
    len_b = len(b)
    counter_a = 0
    counter_b = 0
    for i in range(len_a + len_b):
        if counter_a == len_a:
            print(*b[counter_b:])
            break
        elif counter_b == len_b:
            print(*a[counter_a:])
            break
        elif a[counter_a] < b[counter_b]:
            print(a[counter_a], end=' ')
            counter_a += 1
        elif a[counter_a] >= b[counter_b]:
            print(b[counter_b], end=' ')
            counter_b += 1

if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    merge(a, b)
