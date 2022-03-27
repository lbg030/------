import sys

N = int(input())

timeTable = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

dp = [0 for i in range(N+1)]

for i in range(N-1, -1, -1):
    if i + timeTable[i][0] > N:
        dp[i] = dp[i+1]
        # print(i)
    else:
      # 현재 일을 맡았을 때 들어오는 보상 + 현재 일을 끝냈을때 들어오는 보상 vs 일을 맡지 않았을때 보상
        dp[i] = max(timeTable[i][1] + dp[i + timeTable[i][0]], dp[i+1])

print(dp[0])
# print(timeTable)
# print(dp)
