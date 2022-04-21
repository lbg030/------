# 2504 괄호의 값

import sys
input = sys.stdin.readline

s = input().strip()
print(s)
stackS = []
stackB = []
coeff = 1
isPaired = True
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        stackS.append(i)
        coeff *= 2
    elif s[i] == '[':
        stackB.append(i)
        coeff *= 3
    elif s[i] == ')':
        if stackS:
            if s[i - 1] == '(':
                ans += coeff
            stackS.pop()
            coeff //= 2
        else:
            isPaired = False
            break
    elif s[i] == ']':
        if stackB:
            if s[i - 1] == '[':
                ans += coeff
            stackB.pop()
            coeff //= 3
        else:
            isPaired = False
            break
    # print(stackS, stackB)
if not stackB and not stackS and isPaired:
    print(ans)
else:
    print(0)
