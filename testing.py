import sys
input = sys.stdin.readline

n = int(input())
tmp = list(map(int,input().split()))
dp1 = tmp; dp2 = tmp
for _ in range(n-1):
    a,b,c = map(int,input().split())
    # dp배열에 append 하는 것이 아니라, 값을 갱신시켜준다.
    dp1 = [a+max(dp1[0],dp1[1]),b+max(dp1),c+max(dp1[1],dp1[2])]
    dp2 = [a+min(dp2[0],dp2[1]),b+min(dp2),c+min(dp2[1],dp2[2])]
print(max(dp1),min(dp2))