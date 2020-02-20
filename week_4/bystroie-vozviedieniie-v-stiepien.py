import math


def power(a, n):
    if n == 0:
        result = 1
    elif n % 2 == 0:
        result = power(a ** 2, n / 2)
    else:
        result = a * power(a, n - 1)

    return result


if __name__ == "__main__":
    a = float(input())
    n = int(input())
    print(power(a, n))
