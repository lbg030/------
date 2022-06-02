n = int(input())
dp = [0] * (n+1)
dp[1] = 9

if n == 1:
    print(dp[n])
else :
    dp[2] = 17
# 9 17 32 61 116
#  8 15 29 57
    for i in range(3, n+1):
        dp[i] = (dp[i-1] * 2) - (i-1)

    print(dp[n])
    print(dp)