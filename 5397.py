n = int(input())

for _ in range(n):
    left = []
    right = []
    cmd = input()

    for i in cmd:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
        # print(left, right)
    left.extend(reversed(right))

    print(''.join(left))
