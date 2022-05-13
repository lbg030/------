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

print(dic.keys(), dic.values())

a = list(dic.keys())
b = list(dic.values())

print(a,b)
print(len(a),sum(b[0]), len(b), sum(b[1]))

print(max(sum(b[0]),sum(b[1])))