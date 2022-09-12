n, l = map(int, input().split())
pot = [list(map(int, input().split())) for _ in range(n)]
pot.sort()
cur = pot[0][0]
answer = 0
for s, e in pot:
    if cur > e:
        continue
    elif cur < s:
        cur = s
    if (e-cur)%l == 0:
        answer += (e-cur)//l
        cur += ((e-cur)//l) * l
    else:
        answer += (e-cur)//l + 1
        cur += ((e-cur)//l + 1) * l
print(answer)