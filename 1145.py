a = list(map(int, input().split()))

# print(a)

ans = 1
count = 0
value = 0

while(True):
    for i in a:
        if (ans % i == 0):
            count += 1

    if(count >= 3):
        print(ans)
        break
    else:
        ans += 1
        count = 0

# combinations => 리스트 안의 모든 경우의 수
# from itertools import combinations
# from math import lcm
# m = 1000000
# arr = list(map(int, input().split()))
# for a,b,c in list(combinations([0,1,2,3,4], 3)):
#     m = min(m, lcm(arr[a], arr[b], arr[c]))
# print(m)
