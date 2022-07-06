from sys import stdin

n, m = map(int, input().split())

li = list(map(int, stdin.readline().rstrip().split()))

start, end = 1, max(li)  # 이분탐색 검색 범위 설정

while (start <= end):
    log = 0

    mid = (start + end) // 2

    for x in li:
        if(x >= mid):
            log += x - mid

    if(log >= m):
        start = mid + 1

    else:
        end = mid - 1
print(end)
