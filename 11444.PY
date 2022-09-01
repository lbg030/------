
n = int(input())

lst = [[1,1],[1,0]]
tlst = [[1,1],[1,0]]

for _ in range(n-1):
    a = tlst[0][0] * lst[0][0] + tlst[0][1] * lst[1][0] 
    b = tlst[0][0] * lst[0][1] + tlst[0][1] * lst[1][1] 
    c = tlst[1][0] * lst[0][0] + tlst[1][1] * lst[1][0] 
    d = tlst[1][0] * lst[0][1] + tlst[1][1] * lst[1][1] 
    
    tlst = [[a,b],[c,d]]

print(tlst[-1][-1] % 1000000007)
    