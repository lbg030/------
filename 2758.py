#2001개에 대하여 모든 경우의수를 계산해 놔야함.
#점화식을 찾지 못하면 못푼다고 함

#모든 경우의 수
# 0 ~ 10 까지의 경우의 수
dp = [[0]*2001 for i in range(11)]

#m이 뭐든지간에 n이 0이면 0개의 수로 로또를 맞추는 거기 때문에 무조건 한개의 경우의 수 그래서 dp[0]은 1로 맞춤
dp[0] = [1]*2001

#점화식
for i in range(1, 11):
    for j in range(1, 2001):
        dp[i][j] = dp[i][j-1]+dp[i-1][j//2]

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(dp[n][m])

# print(dp[4][:11])