
n = int(input())
# 1 2 3 5 7 12
dp = [0] * (n+2)
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    a = (dp[i-2] + dp[i-1]) % 15746
    dp[i] = a
print(dp[n])
# print(dp)
