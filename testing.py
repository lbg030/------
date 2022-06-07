## 1번

for i in range(1, 101):
    if i % 5 == 0 or i % 7 == 0:
        continue
    print(i)
    
## 2번

num = 0
while True:
    if num >= 30 : break
    print(num)
    num += 1