# 2나 3을 더한다는 개념이 아닌 무조건 2 or 3을 곱한다는 개념.

def solve(lst):
    for i in range(len(lst)):
        if(lst[i] == ')'):
            if(stack[-1] != '('):
                return 0
            else:
                if(len(stack) > 1):
                    tempList.append(2)
                    pass

        elif(lst[i] == ']'):
            if(stack[-1] != '['):
                return 0
            else:


lst = list(input())
stack = []
tempList = []
value = 1
