n = int(input())
t = list(map(int, input().split()))
s_li = sorted(t)
li = []
for i in range(n):
    idx = s_li.index(t[i])
    # print(idx)
    li.append(idx)
    s_li[idx] = 0
    # print(s_li)

print(*li)
