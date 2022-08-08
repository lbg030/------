n,m,l = map(int, input().split())
lst = [0] + list(map(int, input().split())) + [l]
lst.sort()

start, end = 1, l-1
res = 0
while start <= end:
    count = 0
    mid = (start+end) // 2
    for i in range(1, len(lst)):
        # 현재 거리 중 mid보다 큰 거리를 찾아서
        if lst[i]-lst[i-1] > mid:
            # 나눈 만큼 휴게소를 설치 (현재 설치 돼있는 구역은 제외해야해서 -1)
            count += (lst[i]-lst[i-1]-1)//mid
    if count > m:
        start = mid+1
    else:
        end = mid-1
        result = mid
print(result)
 