genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]	
#output = [4, 1, 3, 0]

def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        if genres[i] not in dic :
            dic[i] = [0]
            dic[i].append(plays[i])
        else :
            dic[i].append(plays[i])
    return answer