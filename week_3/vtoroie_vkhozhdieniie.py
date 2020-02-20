import sys
s = input()
index_f = s.find('f')
if index_f == -1:
    print(-2)
    sys.exit(0)
index_s = s[index_f + 1:].find('f')
if index_s != -1:
    index_s += index_f + 1
print(index_s)
