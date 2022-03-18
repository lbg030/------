li = [1, 1, 1]

for i in range(3, 7):
    li.append(li[i-3] + li[i-2])
    print(li)
