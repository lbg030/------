from sys import stdin

n,m,b = map(int, input().split()) #b는 인벤토리에 있는 블록 개수

board = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
#벽돌 제거시 2초 추가시 1초
remove = 2
add = 1

#답
second = 0
#제거해서 맞추는 것과 추가해서 만드는거 비교 하기 위한 리스트
compared = []
