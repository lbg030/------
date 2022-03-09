n = int(input())
li = []
for i in range(n):
    li.append(input())
li = list(set(li))
li.sort()
li.sort(key=len)

for x in li:
    print(x)
