amount = int(input())
values = set(range(1, amount + 1))

while True:
    input_str = input()
    if input_str == 'HELP':
        break
    input_set = set([int(i) for i in input_str.split()])
    input_str = input()
    if input_str == 'YES':
        values.intersection_update(input_set)
    else:
        values.symmetric_difference_update(input_set & values)

if values == set():
    values = set(range(1, amount + 1))

print(*sorted(values))
