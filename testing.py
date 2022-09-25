import sys
input=sys.stdin.readline
from collections import defaultdict

N,K=map(int,input().split())
array=[len(input()) for _ in range(N)]
dic=defaultdict(list)
for i in range(N):
    dic[array[i]].append(i)