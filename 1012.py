testCase = int(input())
for i in range(testCase):
    width, length, cabbage = map(int, input().split()) #가로, 세로, 배추위치
    
    #한칸 더 추가한 이유는 오른쪽과 아래쪽을 비교할 건데 
    # 그래프의 끝에선 인덱스 에러가 나는 것을 방지하기 위해
    graph = [[0] * (width) for _ in range(length)] # 가로 세로만큼 그래프
    cnt = 0
    #배추 위치 심기
    for i in range(cabbage):
        x, y = map(int , input().split())
        graph[y][x] = 1

    print(cnt)
    print(graph)    