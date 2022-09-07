
n = int(input())

lst = [[1,1],[1,0]]
tlst = [[1,1],[1,0]]
p=1000000007

for _ in range(n):
    a = (tlst[0][0] * lst[0][0] + tlst[0][1] * lst[1][0]) %p
    b = (tlst[0][0] * lst[0][1] + tlst[0][1] * lst[1][1]) %p
    c = (tlst[1][0] * lst[0][0] + tlst[1][1] * lst[1][0]) %p
    d = (tlst[1][0] * lst[0][1] + tlst[1][1] * lst[1][1]) %p
    
    tlst = [[a,b],[c,d]]

print(tlst[-1][-1] % p)
# print(tlst[-1][-1] % 1000000007)