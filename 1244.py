from sys import stdin

n = int(stdin.readline().rstrip())
li = list(map(int, stdin.readline().rstrip().split()))

personNumber = int(input())
personList = []

for _ in range(personNumber):
    gender, number = map(int, input().split())
    idx = 1

    # 남학생
    if(gender == 1):
        while number * idx - 1 < n:
            if li[number * idx-1] == 1:
                li[number * idx-1] = 0
            else:
                li[number * idx-1] = 1
            idx += 1
    print(f" 남학생 거쳤을때 {li}")
    # --------------------------------

    if(gender == 2):
        idx = 0
        while True:
            idx += 1
            # number 1 일 경우
            if(number == 1):
                li[0] = 1 if li[0] == 0 else 1
                break
            # ----------------------------------------------------------------

            else:
                if number - idx - 1 < 0 or number + idx - 1 >= len(li):
                    print(" 0보다 작음")
                    for i in range(number - idx, number + idx - 1):
                        if(li[i] == 1):
                            li[i] = 0
                        else:
                            li[i] = 1
                    break

                # number가 3일 때 1이랑 3을 가르켜야함. -> 0 4
                if(li[number - idx - 1] != li[number+idx-1]):
                    print(" 다름 ")
                    print(number - idx - 1, number + idx - 1)
                    for i in range(number - idx - 1, number + idx):
                        if(li[i] == 1):
                            li[i] = 0
                        else:
                            li[i] = 1
                    break

              # print(number - idx - 1)

print(li)
