from sys import stdin

n = int(input())
dic = {}
count = 0
for _ in range(n):
    name, work = stdin.readline().rstrip().split()

    #출근한 사람
    if name not in dic and work == '+':
        dic[name] = 1
    
    #동명이인
    elif name in dic and work == '+':
        dic[name] += 1

    #출근 안찍히고 퇴근만 한 사람
    elif name not in dic and work == '-':
        count += 1
    
    #동명이인 처리[ 만약 어떤 사람이 출근했다가 퇴근하면 dic에 기록이 남음.]
    #따라서 dic.value의 값이 0이면 이미 출퇴근이 이루어 진 것이기 때문에 count값을 늘려주었음.
    elif name in dic and work =='-':
        if dic[name] == 0:
            count += 1
        else :
            dic[name] -= 1

count += sum(dic.values()) 
print(count)