# 유클리드 호제법
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소 공배수
def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
lst = [1] * (n)

cocktail_list = []
graph = {}

for i in range(n-1):
    a,b,p,q = map(int, input().split())

    divided = gcd(p,q) # 기약분수로 만들기 위해
    
    if a not in graph:
        graph[a] = [b]
    else :
        graph[a].append(b)
        
    if b not in graph:
        graph[b] = [a]
    else :
        graph[b].append(a)
        
        
    if divided != 1:
        p = p // divided
        q = q // divided
        
    if lst[a] == 1 and lst[b] == 1:
        # print("LCM",a,b,p,q)
        prev_a = lst[a]
        prev_b = lst[b]
        
        lst[a] = prev_b * p
        lst[b] = prev_a * q
        
        
        for x in graph[a]:
            if x != b:
                lst[x] *= p
        
        for x in graph[b]:
            if x != a:
                lst[x] *= q
    
    else :
        lcm_value = lcm(lst[a], lst[b])
        
        prev_a = lst[a]
        lst[a] = lcm_value * p
        for x in graph[a]:
            if x != b:
                lst[x] *= (lst[a] // prev_a)
        
        prev_b = lst[b]
        lst[b] = lcm_value * q
        for x in graph[b]:
            if x != a:
                lst[x] *= (lst[b] // prev_b)
            
print(*lst)
print(graph)


