n = input()
stack = []
error = 0
for i in range(len(n)):
    if n[i] == '(':
        stack.append(n[i])

    else:
        if stack[-1] == '(':
            stack.pop()
        else:
            error += 1

print(error)
