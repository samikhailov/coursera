with open("input.txt", "r", encoding="utf-8") as f:
    text = " ".join(f.readlines())

words = text.split()
result = dict()
for i in words:
    result[i] = result.get(i, 0)
    print(result[i], end=" ")
    result[i] += 1
print()
