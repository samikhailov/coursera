amount = int(input())
synonyms = {}

for i in range(amount):
    input_list = input().split()
    synonyms[input_list[0]] = input_list[1]
    synonyms[input_list[1]] = input_list[0]

print(synonyms[input()])
