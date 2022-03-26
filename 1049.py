n, m = map(int, input().split())
li = []

for _ in range(m):
    li.append(list(map(int, input().split())))
# print(li)
lower = li[0][0]
lower2 = li[0][1]
for x in li:
    # print(x[0])
    lower = min(lower, x[0])
    lower2 = min(lower2, x[1])
if(n <= 6):
    print(lower)
else:
    print(min(lower * (n // 6) + lower2 * (n % 6), lower * ((n // 6) + 1)))
