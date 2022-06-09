n = int(input())
lst = list(map(int, input().split()))
dp = [0,lst[0]]

if dp[1] * 2 > lst[1] :
        dp.append(dp[1]*2)
else :
        dp.append(lst[1])
        
# dp = [0,1,5]
for i in range(2,n):
    
    dp.append(max(lst[i], dp[i]+dp[1], dp[i-2] + dp[2]))

print(dp)