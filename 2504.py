lst = input()
# 2에 대한 연산 스택
stackTwo = []
# 3에 대한 연산 스택
stackThree = []
value = 1
checked = True
result = 0

for i in range(len(lst)):
    if lst[i] == ')':
        if(stackTwo):
            if(lst[-1] == '('):
                result += value
            else:
                checked = False
                break
            stackTwo.pop()
            value = value // 2
        else:
            checked = False
            break
    elif lst[i] == ']':
        if(stackThree):
            if(lst[-1] == '['):
                result += value
            else:
                checked = False
                break
            stackThree.pop()
            result = result // 3

        else:
            checked = False
            break

    elif lst[i] == '(':
        stackTwo.append(i)
        value *= 2
    elif lst[i] == ']':
        stackThree.append(i)
        value *= 3

if(checked == True):
    if(not stackTwo and not stackThree):
        print(result)
else:
    print(0)
