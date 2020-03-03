if __name__ == "__main__":
    amount_towns = int(input())
    towns = list(enumerate(map(int, input().split()[:amount_towns])))
    amount_shelters = int(input())
    shelters = list(enumerate(map(int, input().split()[:amount_shelters])))
    towns.sort(key=lambda k: k[1])
    shelters.sort(key=lambda k: k[1])

    index = 0
    result = []

    for i in range(amount_towns):
        while index != amount_towns - 1 and abs(
            towns[i][1] - shelters[index][1]
            ) > abs(
            towns[i][1] - shelters[index + 1][1]
        ):
            index += 1
        else:
            result.append([shelters[index][0] + 1, towns[i][0]])
    result.sort(key=lambda p: p[1])
    print(*[i[0] for i in result])
