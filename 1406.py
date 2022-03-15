import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if(command[0] == "L"):
        if st1:
            st2.append(st1.pop())
        else:
            continue
    elif(command[0] == "D"):
        if st2:
            st1.append(st2.pop())
        else:
            continue

    elif(command[0] == "B"):
        if(st1):
            st1.pop()
        else:
            continue
    elif(command[0] == "P"):
        # print(command, command[1])
        st1.append(command[1])

print(''.join(st1 + list(reversed(st2))))
