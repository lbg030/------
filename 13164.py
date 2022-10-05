from sys import stdin
import math

N, K = map(int, input().split())
lst = list(map(int, stdin.readline().rstrip().split()))

if N == K:
    print("0")

# 무조건 2명이상 있는 그룹이 한 개 이상 존재
else :
    result_list = []
    for i in range(1,N):
        result_list.append(lst[i] - lst[i-1])
    result_list.sort()
    
    # print(result_list)
    print(sum(result_list[:N-K]))