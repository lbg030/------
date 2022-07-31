#파이참에서는 돌아가는데 백준에서 런타임 에러💢

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    dp = []
    for i in range(2):
        dp.append(list(map(int, input().split())))

    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for j in range(2, n):
        dp[0][j] += max(dp[1][j - 1], dp[1][j - 2])
        dp[1][j] += max(dp[0][j - 1], dp[0][j - 2])

    print(max(dp[0][n - 1], dp[1][n - 1]))