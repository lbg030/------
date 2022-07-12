from sys import stdin

n, m = map(int ,input().split())
knowTruth = list(map(int, input().split())) # 0이면 0 / 아니면 x, y 형태

party = []

for _ in range(m):
    lst = list(map(int, stdin.readline().rstrip().split()))
    party.append(lst[1:]) # 인원은 상관이 없기 때문에 생략해서 append 한다

cnt = len(party)
# print(party)
# print(cnt)
if len(knowTruth) <= 1:
    print(cnt)
else :
    for x in party :
        for y in knowTruth[1:] :
            if y in x:
                # print(y, x)
                cnt -= 1
                break
        
    print(cnt)