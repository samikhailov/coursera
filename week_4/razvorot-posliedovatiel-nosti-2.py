import sys


def revert():
    current = int(input())
    if current != 0:
        revert()
    print(current)


if __name__ == "__main__":
    revert()
