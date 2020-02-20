import math


def sum(a, b):
    if b == 0:
        result = a
    else:
        result = sum(a + 1, b - 1)
    return result


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(sum(a, b))
