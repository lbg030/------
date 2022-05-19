n = int(input())
metro = []

for q in range(n):
    metro.append(list(map(int,input().split()))[1:])

fin = int(input())
c = [0]; d = []; cnt = 0
while True:
    for i in c:
        for j in range(n):
            if i in metro[j]:
                d = d + metro[j]
            print(f"i = {i}, c = {c},d = {set(d)} ,cnt = {cnt}")
    d = list(set(d))
    if fin in d:
        break
    cnt += 1
    if cnt > n:
        cnt = -1
        break
    c = d
    d = []
print(cnt)