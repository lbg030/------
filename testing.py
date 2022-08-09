# BOJ 2470 두 용액
import sys
input = sys.stdin.readline
N = int(input())
sol = list(map(int, input().split()))
sol.sort()
l, r = 0, N-1
near_zero = 9876543210
zero_l, zero_r = 0, 0

while l<r:
    temp = sol[l]+sol[r]
    if abs(temp) < abs(near_zero):
        near_zero = temp
        zero_l, zero_r = l, r
        if near_zero == 0:
            break
    if temp < 0:
        l += 1
    else:
        r -= 1

print(sol[zero_l], sol[zero_r])