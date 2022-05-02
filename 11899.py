n = input()
stack = []
error = 0
for i in range(len(n)):
    if n[i] == '(':
        stack.append(n[i])

    else:
        if len(stack) > 0:
            if stack[-1] == '(':
                stack.pop()
            else:
                error += 1
        else:
            error += 1
print(error + len(stack))
