lst = input().rstrip()
# 2에 대한 연산 스택
stackTwo = []
# 3에 대한 연산 스택
stackThree = []
value = 1
checked = True
result = 0

for i in range(len(lst)):
    if lst[i] == '(':
        stackTwo.append(i)
        value *= 2
    elif lst[i] == '[':
        stackThree.append(i)
        value *= 3

    elif lst[i] == ')':
        if(stackTwo):
            if(lst[i-1] == '('):
                result += value
            stackTwo.pop()
            value //= 2
        else:
            checked = False
            break
    elif lst[i] == ']':
        if(stackThree):
            if(lst[i-1] == '['):
                result += value
            stackThree.pop()
            value //= 3

        else:
            # print(i)
            # print(stackThree)
            checked = False
            break


if not stackTwo and not stackThree and checked:
    print(result)
else:
    print(0)
