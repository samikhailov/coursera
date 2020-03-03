def get_score(info):
    amount = int(info[0])
    all_applicant = [i.split() for i in info[1:]]
    scores = []
    for i in all_applicant:
        i[-1] = int(i[-1])
        i[-2] = int(i[-2])
        i[-3] = int(i[-3])
        if i[-1] >= 40 and i[-2] >= 40 and i[-3] >= 40:
            scores.append(sum([i[-1], i[-2], i[-3]]))
    scores.sort(reverse=True)

    if amount >= len(scores):
        return 0

    for i in scores[:amount + 1]:
        if scores[0] != i:
            break
    else:
        return 1

    position = amount - 1
    while scores[position] == scores[position + 1]:
        position -= 1

    return scores[position]


with open('input.txt', 'r', encoding='utf8') as f:
    info = [i.rstrip() for i in f.readlines()]

with open('output.txt', 'w', encoding='utf8') as f:
    print(get_score(info), file=f)
