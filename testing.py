land=[[1,2,3,5],[5,6,7,8],[4,3,2,1]]

def solution(land):
    answer = 0
    map =[]
    for i in land:
        map.append(i)
    
    for i,value in enumerate(map):
        if i==0:
            continue
        x = max(map[i-1][1],map[i-1][2], map[i-1][3])
        map[i][0] += x
        x = max(map[i-1][0],map[i-1][2], map[i-1][3])
        map[i][1] += x
        x = max(map[i-1][0],map[i-1][1], map[i-1][3])
        map[i][2] += x
        x = max(map[i-1][0],map[i-1][1], map[i-1][2])
        map[i][3] += x