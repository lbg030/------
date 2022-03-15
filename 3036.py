from math import gcd


n = int(input())
li = list(map(int, input().split()))

# print(li)

for i in range(1, n):
    if (gcd(li[0], li[i]) == 1):
        print(f"{li[0]}/{li[i]}")
    else:
        print(f"{li[0] // gcd(li[0], li[i])}/{li[i] // gcd(li[0], li[i])}")
