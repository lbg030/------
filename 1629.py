a,b,c = map(int, input().split())

def solution(k):
    if k == 1:
        return a % c 
    
    if k % 2 == 0 :
        left = solution(k//2)
        return left * left % c
    else:
        left = solution(k//2)
        return left * left * a % c

print(solution(b))