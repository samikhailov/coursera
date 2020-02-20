import sys


def revert(prev):
    if prev == 0:
        print(prev)
        sys.exit(0)
    current = int(input())
    if current == 0:
        print(current)
        print(prev)
        return True
    else:
        if revert(current):
            print(prev)
            return True
        return False


if __name__ == "__main__":
    revert(int(input()))
