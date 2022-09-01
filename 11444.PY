import numpy as np

lst = np.array([[1,1],[1,0]])

n = int(input())
tlst = lst
for _ in range(n):
    tlst = tlst @ lst
    tlst = tlst % 1000000007
print(tlst[-1][-1])
# print(tlst)