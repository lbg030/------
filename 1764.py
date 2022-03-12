# n, m = map(int, input().split())
# dh = set()
# ds = set()
# for i in range(n):
#     dh.add(input())

# for j in range(m):
#     ds.add(input())

# # print(f"dh = {dh} ds = {ds}")
# res = list(dh & ds)
# print(len(res))
# for x in sorted(res):
#     print(x)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dont_hear = set()
dont_see = set()
answer = []
for i in range(N):
    dont_hear.add(input().rstrip())
for i in range(M):
    dont_see.add(input().rstrip())
answer = list(dont_see & dont_hear)
answer.sort()
print(len(answer))
for i in answer:
    print(i)
