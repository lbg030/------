a, b, c = map(int, input().split())
X = input()
Y = input()

dp = [[0]*(len(X)+1) for i in range(len(Y)+1)]

print(dp)
for i in range(1, len(X)+1):
    dp[0][i] = dp[0][i-1] + b
for i in range(1, len(Y)+1):
    dp[i][0] = dp[i-1][0] + b

print(dp)
for i in range(1, len(Y)+1):
    for j in range(1, len(X) + 1):
        if X[j-1] == Y[i-1]:
            dp[i][j] = dp[i-1][j-1] + a
        else:
            dp[i][j] = max(dp[i-1][j-1] + c, dp[i-1]
                           [j] + b, dp[i][j-1] + b)
print(dp)
print(dp[len(Y)][len(X)])

# https://www.acmicpc.net/problem/2216
