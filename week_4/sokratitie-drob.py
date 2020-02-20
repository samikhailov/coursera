import math


def ReduceFraction(n, m):
    for i in range(min(n, m), 1, -1):
        if n % i == 0 and m % i == 0:
            return (int(n / i), int(m / i))
    return (n, m)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    print(*ReduceFraction(n, m))
