n = int(input())

for _ in range(n):
    m = int(input())
    li = [False] + [True] * m
    for i in range(2, m+1):
        for j in range(i, m+1, i):
            # print(j)
            # print(li)
            if(li[j] == True):
                li[j] = False
            else:
                li[j] = True
    print(li.count(True))
