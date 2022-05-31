n = 1

#답
answerfor = 0
answerwhile = 0

# while 문으로 하기
while n < 11 :
    answerwhile = answerwhile + n
    n = n + 1 #이 부분을 안해주면 n이 계속 1로 고정되어서 while문 탈출 불가능
    
# for 문
for i in range(11):
    answerfor = answerfor + i # 0부터 10까지 더해짐
    
print(answerfor, answerwhile)
        