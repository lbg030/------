# 유클리드 호제법
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소 공배수
def lcm(a, b):
    return a * b / gcd(a, b)


n = int(input())
lst = [1] * (n)

cocktail_list = []
graph = {}

for i in range(n-1):
    a,b,p,q = map(int, input().split())
    cocktail_list.append((a,b,p,q))
    
    if a not in graph:
        graph[a] = [b]
    else :
        graph[a].append(b)
        
    if b not in graph:
        graph[b] = [a]
    else :
        graph[b].append(a)
        
for a,b,p,q in cocktail_list:
    divided = gcd(p,q) # 기약분수로 만들기 위해
    if divided != 1:
        p = p // divided
        q = q // divided
        
    


# 1 1 3 4
# 3 1 3 4
# 3과 4의 최소공배수 * 5 와 *7 - > 12 * 5 ; 12 * 7
# 60 20 63 84
