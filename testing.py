n = int(input())
subway = []
for _ in range(n):
    subway.append(list(map(int,input().split()))[1:])
destination = int(input())

#시작점은 무조건 0에서 시작
start = [0]
#갈 수 있는 경로를 저장하는 임시 리스트
lst = []
#환승한 횟수
cnt = 0

while True:
    #환승으로 갈 수 있는 곳
    for x in start:
        #subway 모든 호선 돌리기
        for j in range(n) :
            #만약에 환승으로 갈 수 있는 곳이 있으면 임시리스트에 추가
            if x in subway[j]:
                lst += subway[j]
    #중복이 무조건 생기기 때문에 set으로 중복 제거
    lst = set(lst)
    if destination in lst :
        print(cnt)
        break
    else :
        cnt += 1
    #n보다 크다는건 못간다는 걸 의미    
    if cnt > n:
        print(-1)
        break
    #두번째 부터는 시작점이 갈 수 있는 경로로 변경됨.
    start = lst
    #다시 start에서 갈수 있는 경로를 저장해야 함으로 초기화
    lst = []