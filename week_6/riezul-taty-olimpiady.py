n = int(input())
member = []

for i in range(n):
    member.append(input().split())


print(*[i[0] for i in sorted(member, key=lambda k: int(k[1]), reverse=True)],
      sep='\n')
