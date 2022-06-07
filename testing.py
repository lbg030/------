player1 = []
player2 = []

for _ in range(3):
    player1.append(input())

for _ in range(3):
    player2.append(input())
    
# print(player1, player2)

def game(shape, color, number):
    
    #처음에 숫자는 str
    number = int(number)
    result = 0
    
    if shape == 'HEART' :
        #빨간색 하트
        if color == 'RED':
            result = number * 2
        #초록색 하트
        else :
            result = number - 1
    
    if shape == 'CLOVER':
        #빨간색 클로버
        if color == 'RED':
            result = 0
        #초록색 클로버
        else :
            result = number + 2
    
    #결과값 출력
    return result

player1 = game(player1[0],player1[1],player1[2])
player2 = game(player2[0],player2[1],player2[2])

if player1 > player2 :
    print("player1 win, player2 lose")
elif player2 > player1 :
    print("player1 lose, player2 win")
else :
    print("draw")
    
