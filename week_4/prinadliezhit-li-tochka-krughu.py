def IsPointInCircle(x, y, xc, yc, r):
    if (y - yc) ** 2 + (x - xc) ** 2 <= r ** 2:
        return True
    return False


if __name__ == "__main__":
    x, y = float(input()), float(input())
    xc, yc = float(input()), float(input())
    r = float(input())

    if IsPointInCircle(x, y, xc, yc, r):
        print('YES')
    else:
        print('NO')
