li = []
for _ in range(int(input())):
    m = int(input())
    if(len(li) == 0 and m == 0):
        li.append(m)

    if(m == 0):
        li.pop()
    else:
        li.append(m)

print(sum(li))
