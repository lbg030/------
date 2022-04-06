import sys
input = sys.stdin.readline

s = []


def boj(command, x):
    global s
    if command == "add":
        if x not in s:
            s.append(x)
    elif command == "remove":
        if x in s:
            s.remove(x)
    elif command == "check":
        if x in s:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if x in s:
            s.remove(x)
        else:
            s.append(x)
    elif command == "all":
        s = [i for i in range(1, 21)]
    elif command == "empty":
        s = []


M = int(input())

for _ in range(M):
    command = input().strip()
    if command == "all" or command == "empty":
        boj(command, 0)
    else:
        command, x = command.split()
        boj(str(command), int(x))
