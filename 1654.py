n, m = map(int, input().split())

li = []
for i in range(n):
    li.append(int(input()))

start, end = 1, max(li)

while start <= end:
    mid = (start+end) // 2
    count = 0
    for x in li:
        count += x // mid

    if(count >= m):
        start = mid + 1
    else:
        end = mid - 1

print(end)
