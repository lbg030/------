n = int(input())

dp = [0] * (n+1)
if n == 1:
    dp[1] = 'SK'
else :
    dp[2] = 'CY'

    for i in range(3, n+1):
        if i   2 == 0 :
            dp[i] = 'CY'
        else :
            dp[i] = 'SK'
            
print(dp[n])