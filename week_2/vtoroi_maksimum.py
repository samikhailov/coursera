import sys
seq = []
while True:
    num = input().split('\n')
    seq += num
    if '0' in num:
        seq = [int(i) for i in seq]
        seq.remove(max(seq))
        print(max(seq))
        sys.exit(0)
