def revert(sum):
    num = int(input())
    if num != 0:
        sum += revert(num)
    return sum


if __name__ == "__main__":
    print(revert(0))
