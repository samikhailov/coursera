import math


def MinDivisor(n):
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


if __name__ == "__main__":
    n = int(input())
    print(MinDivisor(n))
