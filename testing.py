dic = {}
lst = [1,2,3,4]
for i in range(len(lst)):
    if lst[i] in dic :
        dic[lst[i]] += 1 
    else :
        dic[lst[i]] = 1

print(dic)