
n = int(input())

lst = [[1,1],[1,0]]
tlst = [[1,1],[1,0]]

for _ in range(n):
    tlst[0][0] = tlst[0][0] * lst[0][0] + tlst[0][1] * lst[1][0]
    tlst[0][1] = tlst[0][0] * lst[0][1] + tlst[0][1] * lst[1][1]
    tlst[1][0] = tlst[1][0] * lst[0][0] + tlst[1][1] * lst[1][0]
    tlst[1][1] = tlst[1][0] * lst[0][1] + tlst[1][1] * lst[1][1]
    
    # print(n)
    print(tlst)
    lst = tlst[:]

# print(tlst[-1][-1])
    