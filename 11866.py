n, m = map(int, input().split())

n = [i for i in range(1, n+1)]
cnt = 0
res = []

while len(n) > 0:
    cnt += m-1
    # print(f"cnt = {cnt}, n = {n}, len(n) = {len(n)}")
    while(cnt > len(n) - 1):
        cnt = cnt - len(n)
    res.append(n[cnt])
    del n[cnt]

print("<", end="")
for x in res:
    if(x == res[-1]):
        print(x, end="")
    else:
        print(x, ", ", sep='', end="")
print(">")
