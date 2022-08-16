#  K = K-(K&((~K)+1))

a = int(input())

binary_k = '0b' + input()
cnt = 0
def not_binary(n):
    k = ''
    for i in range(2, len(n)):
        if n[i] == '1' :
            k += '0'
        else :
            k += '1'
    return int(k,2)

def decimal_to_binary(n):
    return bin(n)
        


while True:
    k = (((not_binary(bin(a))) + 1))
    middle = a&k
    
    res = a - middle
    print(res)
    if res == 0:
        print(cnt)
        break
    else :
        cnt += 1
        a = res