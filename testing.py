genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]	

dic = {}

for i in range(len(genres)):
        genresDic = genres[i] 
        if genres[i] not in dic :    
            dic[genresDic] = [0]
            dic[genresDic].append(plays[i])
        else :
            dic[genresDic].append(plays[i])

# print(dic.keys(), dic.values())
lst = []
a = list(dic.keys())
b = list(dic.values())
for i in b :
    lst.append(sum(i))
print(a)
print(lst)
ranking = []
for i in lst :
    ranking.append(sorted(lst, reverse=True).index(i))
print(ranking)
print(dic)
for i in range(len(ranking)):
    for j in range(len(plays)):
        pass