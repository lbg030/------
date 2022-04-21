def solve():
    data = input()
    score = 0
    temp = 1

    stack = []
    for i in range(len(data)):

        if data[i] == '(':
            stack.append(data[i])
            temp *= 2

        elif data[i] == '[':
            stack.append(data[i])
            temp *= 3

        elif data[i] == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return 0
            if data[i - 1] == '(':
                score += temp
            temp //= 2
            stack.pop()

        elif data[i] == ']':
            if len(stack) == 0 or stack[-1] != '[':
                return 0
            if data[i - 1] == '[':
                score += temp
            temp //= 3
            stack.pop()

    return score if len(stack) == 0 else 0
