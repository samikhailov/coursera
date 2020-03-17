with open('input.txt', 'r', encoding='utf-8') as f:
    amount = len(set(' '.join(f.readlines()).split()))
    print(amount)
