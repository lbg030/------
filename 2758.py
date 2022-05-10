#로또
#이게 왜 DP문제지
# 1 2 4 8
# 1 2 4 9
# 1 2 4 10
# 1 2 5 10

test = int(input())
for _ in range(test):
    n, m = map(int, input().split())

dp = [i for i in range(1, m+1)]
print(dp)