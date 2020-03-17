words = {}


with open("input.txt", "r", encoding="utf-8") as f:
    text = " ".join(f.readlines())
input_list = text.split()

for i in input_list:
    words[i] = words.get(i, 0)
    words[i] += 1

words_list = list(words.items())
words_list.sort(key=lambda k: k[0])
words_list.sort(key=lambda k: k[1], reverse=True)

print(*[i[0] for i in words_list], sep='\n')
