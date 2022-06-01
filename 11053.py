n = int(input())
li = list(map(int, input().split()))
dp = [1] * n
# print(li)
for i in range(n):
    for j in range(i):
        if(li[i] > li[j]):
            # print(f"dp = {li[j]}, i = {i} j = {dp[j]}")
            # print(dp)
            dp[i] = max(dp[i], dp[j]+1)
            # print(dp[i])

print(max(dp))