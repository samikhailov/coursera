s = input()
index_f = s.find('f')
index_l = s.rfind('f')
if index_f == -1:
    pass
elif index_f == index_l:
    print(index_f)
else:
    print(index_f, index_l)
