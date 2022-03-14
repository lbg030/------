li = sorted([input()[0] for _ in range(int(input()))])
s = set(li)
res = []

for x in s:
    if(li.count(x) >= 5):
        res.append(x)

print(''.join(sorted(res)) if len(res) > 0 else "PREDAJA")
# print(s, li)
