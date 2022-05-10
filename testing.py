clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

dic = {}
categoryList = []
cnt = 0

for x,y in clothes:
    if y not in dic :
        dic[y] = [x]
        categoryList.append(y)
    else :
        dic[y].append(x)
        
if len(categoryList) == 1 :
    cnt = len(dic[categoryList[0]])
else :
    mul = 1
    for x in categoryList:
        cnt += len(dic[x])
        mul *= len(dic[x])
    cnt += mul
print(cnt)