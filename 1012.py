testCase = int(input())
for i in range(testCase):
    width, length, cabbage = map(int, input().split()) #가로, 세로, 배추위치
    
    #한칸 더 추가한 이유는 오른쪽과 아래쪽을 비교할 건데 
    # 그래프의 끝에선 인덱스 에러가 나는 것을 방지하기 위해
    graph = [[0] * (width+1) for _ in range(length+1)] # 가로 세로만큼 그래프
    cnt = 0
    #배추 위치 심기
    for i in range(cabbage):
        x, y = map(int , input().split())
        graph[y][x] = 1

    #그래프 탐색
    for i in range(width):
        for j in range(length):
            if graph[j][i] == 1:
                if graph[j+1][i] == 0 and graph[j][i+1] == 0:
                    print(j, i)
                    cnt += 1
    print(cnt)
    print(graph)