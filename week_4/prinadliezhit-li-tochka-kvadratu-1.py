def IsPointInSquare(x, y):
    if -1 <= x and x <= 1 and -1 <= y and y <= 1:
        return True
    return False


if __name__ == "__main__":
    x, y = float(input()), float(input())
    if IsPointInSquare(x, y) is True:
        print('YES')
    else:
        print('NO')
