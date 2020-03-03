rows = []
with open('input.txt', 'r', encoding='utf8') as f:
    info = [i.rstrip().split() for i in f.readlines()]


with open('output.txt', 'w', encoding='utf8') as f:
    for i in sorted(info):
        print(i[0], i[1], i[3], file=f)
