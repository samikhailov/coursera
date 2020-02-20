import sys
seq = []
while True:
    num = input().split('\n')
    seq += num
    if '0' in num:
        print(seq.index('0'))
        sys.exit(0)
