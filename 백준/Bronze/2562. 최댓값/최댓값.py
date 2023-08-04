list = []
for b in range(0,9):
    a = int(input())
    list.append(a)
limit = max(list)
s = list.index(limit)+1
print(limit)
print(s)