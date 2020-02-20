import sys
seq = []
while True:
    num = input().split('\n')
    seq += num
    if '0' in num:
        seq = [int(i) for i in seq]
        max_eq_seq = 1
        counter = 1
        for i in range(len(seq) - 1):
            if seq[i] == seq[i + 1]:
                counter += 1
            else:
                if counter > max_eq_seq:
                    max_eq_seq = counter
                counter = 1
        print(max_eq_seq)
        sys.exit(0)
