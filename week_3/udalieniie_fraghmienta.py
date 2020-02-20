s = input()
index_f = s.find('h')
index_l = s.rfind('h')
print(s[:index_f] + s[index_l+1:])
