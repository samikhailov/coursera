import math


def MinDivisor(n):
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


def IsPrime(n):
    if MinDivisor(n) == n:
        return True
    else:
        return False


if __name__ == "__main__":
    n = int(input())
    if IsPrime(n):
        print("YES")
    else:
        print("NO")
