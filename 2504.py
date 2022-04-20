Parentheses = []
Brackets = []

inputValue = input()
flag = True
result = 0
coeff = 1

for i in range(len(inputValue)):
    if inputValue[i] == '(':
        Parentheses.append(i)
        coeff *= 2
    elif inputValue[i] == '[':
        Brackets.append(i)
        coeff *= 3
    elif inputValue[i] == ')':
        if Parentheses:
            if inputValue[i-1] == '(':
                result += coeff
            Parentheses.pop()
            coeff //= 2
        else:
            flag = False
            break
    else:
        if Brackets:
            if inputValue[i-1] == '[':
                result += coeff
            Brackets.pop()
            coeff //= 3
        else:
            flag = False
            break

if not Parentheses and not Brackets and flag:
    print(result)
else:
    print(0)
