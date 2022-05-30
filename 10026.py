n = int(input())

Cowgraph = [list(input()) for _ in range(n)]
notCowgraph = []

#G -> R로 변경
for x in Cowgraph:
    tempList = []
    for k in x:
        temp = k.replace("G","R")
        tempList.append(temp)
    notCowgraph.append(tempList)

Cowcnt = 0
notCowCnt = 0

def notCowArt(x,y):
    pass

def cowArt(x,y):
    pass

for x in range(n):
    for y in range(n):
        if Cowgraph[x][y] == Cowgraph[x][y+1]:
            notCowArt(x,y)
            cowArt(x,y)
                            
