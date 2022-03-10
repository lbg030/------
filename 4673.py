n = [q for q in range(1, 10000)]
li = []
for i in n:
    if(i < 10):
        li += [2, 4, 6, 8, 10, 12, 14, 16, 18]
        continue
    elif(100 > i >= 10):
        li.append(((i // 10) + i % 10 + i))
    elif(1000 > i >= 100):
        li.append(i + (i // 100) + ((i % 100) // 10) + i % 10)
    else:
        li.append(i + (i // 1000) + ((i % 1000) // 100) +
                  ((i % 100) // 10) + i % 10)
li = list(set(li))

for x in li:
    if(x >= 10000):
        continue
    else:
        n[x-1] = 0

n = list(set(n))
n.sort()
del n[0]

for k in n:
    print(k)
