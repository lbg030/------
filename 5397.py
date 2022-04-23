# 스택 두개를 이용
# 스택 한개 했더니 시간 초과

# left와 right를 나누어서 그 중간을 커서라고 생각.
# 마지막에는 결국 리버스를 해줘야함 . append이기 때문에 계속 끝으로 저장이 되는데
# 그러면 결국 뒤집어 줘야함

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
