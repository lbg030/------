from collections import deque
n = int(input())

sentence = [deque(input().split()) for _ in range(n)]
possible = deque(input().split())

# i i
# i found interesting cave
# i found i an i cave interesting 이 구문을 처리해줘야됨.

while True:
    check = 0
    for i in range(n):
        if len(sentence[i]) > 0:
            if sentence[i][0] == possible[0]:
                sentence[i].popleft()
                possible.popleft()
                check = 1
                # print("1")
                break

    if check == 0:
        print("Impossible")
        print(possible)
        break

    if len(possible) == 0:
        print("Possible")
        break
