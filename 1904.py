
n =int(input())
# 1 2 3 5 7 12
dp = [0,1,2] # dp[i-2] * 2 +1
if n == 1:
    print(dp[0])
elif n == 2:
    print(dp[1])
else :
    for i in range(3,n+1):
        a = dp[i-2] + dp[i-1]
        if a >= 15746 :
            a %= 15746
        dp.append(a)
    print(dp[n])
    # print(dp)