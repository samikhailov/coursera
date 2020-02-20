import sys
seq = []
while True:
    num = input().split('\n')
    seq += num
    if '0' in num:
        seq = [int(i) for i in seq]
        max_num = max(seq)
        counter = 0
        for i in seq:
            if max_num == i:
                counter += 1
        print(counter)
        sys.exit(0)
