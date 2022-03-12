n, m = map(int, input().split())
n = [i for i in range(1, n+1)]
li = list(map(int, input().split()))

count = 0
todo = 0
# print(f" n = {n}, m = {m}, li = {li}")


while (m != 0):
    # print(f"n = {n}")
    if(n[0] == li[todo]):
        m -= 1
        todo += 1
        del n[0]
        # print(count)
        # print(f" n = {n}")

    elif(n.index(int(li[todo])) <= (len(n) / 2)):  # 왼쪽으로 밀기
        count += 1
        temp = n[0]
        n.insert(len(n), temp)
        del n[0]
    else:  # 오른쪽으로 밀기
        count += 1
        temp2 = n[-1]
        n.insert(0, temp2)
        del n[-1]

print(count)
