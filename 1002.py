# (x - n) ** 2 + (y-m) ** 2 = k**2
# (x - n2) ** 2 + (y-m2) ** 2 = k2**2
import math

count = int(input())
for i in range(count):
    n, m, k, n2, m2, k2 = map(int, input().split())
    distance = math.sqrt((n-n2) ** 2 + (m - m2) ** 2)

    if(distance == 0 and k == k2):
        print("-1")
    elif(abs(k2-k) < distance < abs(k2+k)):
        print("2")
    elif(distance == abs(k2-k) or distance == k2+k):
        print("1")
    else:
        print("0")
