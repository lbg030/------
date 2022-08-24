n,m,s = map(int, input().split())
graph = [list(input()) for _ in range(n)]
target = input()

def left_or_right(lst, alpha, y):
    ans = ''
    value = lst.index(alpha) - y 
    if value < 0 :
        ans += 'L' * abs(value)
    
    else :
        ans += 'R' * abs(value)
    
    ans += 'P'
    return ans