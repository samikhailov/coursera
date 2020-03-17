score = {}

with open("input.txt", "r", encoding="utf-8") as f:
    candidates = f.readlines()

amount_candidates = len(candidates)
for i in candidates:
    score[i] = score.get(i, 0)
    score[i] += 1 / amount_candidates

result = list(score.items())
result.sort(key=lambda k: k[1], reverse=True)

with open("output.txt", "w", encoding="utf-8") as f:
    if result[0][1] > 0.5:
        print(result[0][0], file=f)
    else:
        print(result[0][0], result[1][0], sep="", file=f)
