lst = list(map(str, input().split('`')))
n = 1
while True:
    str= ''
    for x in lst:
        for y in x:
            try :
                str += chr(ord(y)-n)
            except:
                str += y
    if "세명" in str:
        break
    
    n += 1
print(str)
