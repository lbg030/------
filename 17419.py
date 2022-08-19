#  K = K-(K&((~K)+1))
# 51 점 짜리
# a = int(input())
# def not_binary(n):
#     n = bin(n)
#     k = ''
#     for i in range(2, len(n)):
#         if n[i] == '1' :
#             k += '0'
#         else :
#             k += '1'
#     return int(k,2)

# binary_k = '0b' + input()
# decimal_k = int(binary_k,2)
# cnt = 1

# while True:
#     res = (decimal_k ^ (decimal_k & (not_binary(decimal_k) + 1)))
    
#     if res == 0 :    
#         print(cnt)
#         break
    
#     else :
#         decimal_k = res
    
#     cnt += 1

# 100 점
n = input()
a = input()
print(a.count('1'))