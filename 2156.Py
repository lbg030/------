n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))

#DP list 
dp = [0]*n

dp[0] = lst[0]

#만약 n이 2개 일 경우 2개 다 먹는게 이득
#2개 이상일 경우에는 비교 index 확보
if n > 1:
    dp[1] = lst[0]+lst[1]

#만약 n이 3인 경우 세개 중 제일 큰 값 픽
#3개 이상일 경우에 비교 index 확보
if n > 2:
    dp[2] = max(lst[2]+lst[1], lst[2]+lst[0], dp[1])

#3 이상인 경우에 돌리기
for i in range(3, n):
    # 하나도 선택X, 두번째꺼와 이번것 [ 2 0 ], [3 1 0]
    dp[i] = max(dp[i-1], dp[i-2] + lst[i], dp[i-3] + lst[i-1] + lst[i])
    # print("for")

# print(dp)
print(dp[n-1])
