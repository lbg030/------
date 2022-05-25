import re
#re 정규식 이용
t = int(input())
for i in range(t):
    a = input()
    p = re.compile('(100+1+|01)+')
    
    if p.fullmatch(a):
        print("YES")
    else:
        print("NO")