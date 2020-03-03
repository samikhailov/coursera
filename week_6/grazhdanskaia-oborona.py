amount_towns = int(input())
towns = list(enumerate(map(int, input().split()[:amount_towns]), 1))
amount_shelters = int(input())
shelters = list(enumerate(map(int, input().split()[:amount_shelters]), 1))
towns.sort(key=lambda k: k[1])
shelters.sort(key=lambda k: k[1])

index = 0
result = []

for town in towns:
    while (index + 1 < amount_shelters and abs(
            town[1] - shelters[index][1]) > abs(
            town[1] - shelters[index + 1][1])):
        index += 1
    else:
        result.append([town[0], shelters[index][0]])


print(*[i[1] for i in sorted(result, key=lambda k: k[0])])
