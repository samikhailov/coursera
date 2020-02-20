import sys
seq = []
while True:
    num = input().split('\n')
    seq += num
    if '0' in num:
        print(len([int(i) for i in seq[:seq.index('0')] if int(i) % 2 == 0]))
        sys.exit(0)
