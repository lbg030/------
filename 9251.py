a = list(input())
b = list(input())
dp = list([0] * (len(a)-1))


for x in a:
    if x not in b:
        a.remove(x)

cnt = 0
temp = b[:]
for x in a :
        if x in temp :
            start = temp.index(x)
            cnt += 1
            if start + 1 > len(temp)-1 :
                break
            temp = temp[start+1:]
        else :
            continue

print(cnt)