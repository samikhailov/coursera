if __name__ == "__main__":
    free_space, amount_users = map(int, input().split())
    data = []
    tmp = 0
    max_users = 0
    for i in range(amount_users):
        data.append(int(input()))
    data.sort()
    for i in data:
        tmp += i
        if free_space <= tmp:
            break
        else:
            max_users += 1
    print(max_users)
