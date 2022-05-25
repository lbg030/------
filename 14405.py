
target = input()
lst = ["pi","ka","chu"]
checked =''
for x in target :    
    checked += x
    # print(checked)
    if checked in lst :
        checked = ''

if checked :
    print('NO')
else :
    print('YES')