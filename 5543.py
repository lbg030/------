li = []
for i in range(5):
    li.append(int(input()))

burger = min(li[:3])
drink = min(li[3:])

print(burger + drink - 50)
