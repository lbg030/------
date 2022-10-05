# 임의의 회의 K(1≤ K ≤ N)는 회의 K − 1과 회의 K + 1과는 회의 시간이 겹치고 다른 회의들과는 회의 시간이 겹치지 않는다.

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

dp = [0] * n

for i in range(n):
   if i == 0:
       dp[i] = lst[i][2]
    
   elif i == 1:
       dp[i] = max(dp[0], lst[i][2])
    
   else :
       dp[i] = max(dp[i-2] + lst[i][2], dp[i-1])
       
print(dp)