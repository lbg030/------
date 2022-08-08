# 리스트 안에 집어넣어 계산하면 한 지점부터 다른 지점까지에 대해 2개는 가능하지만 3개 이상으로 가면 3분할 4분할이 되지 않음
# 리스트 append 대신 값 자체를 찾는 방식으로 생각

n,m,l = map(int, input().split())
# n이 0일수도 있기 때문에 예외 처리
if n :
    lst = [0] + list(map(int, input().split())) + [l]
else :
    lst = [0,l]

lst.sort()
start,end = 1,l # start = 0 으로 하면 특정 케이스에서 zerodivisionerror 발생
res = 0

while start <= end:
    cnt = 0 # m을 만족하는지 만족 못하는지 점검
    mid = (start + end) // 2
    
    for i in range(len(lst)-1):
        if lst[i+1]- lst[i] > mid:
            cnt += (lst[i+1] - lst[i]) // mid
            
            # 딱 나누어 떨어진 경우에 이미 세워진 곳에 하나를 더 세우는 것이기 때문에 빼줘야 한다.
            if (lst[i+1]- lst[i]) % mid == 0:
                cnt -= 1
            
    if cnt > m:
        start = mid + 1
    else :
        end = mid - 1
        res = mid
        # print(res)
print(res)