a = ['<', 'a', 'b', ' ', 'c', 'd', '>', 'e', 'f']
s = ''
s += ''.join(a[1:5])
# print(''.join(a[1:5]))
# s.append(a[1:5])
print(a[3])
s += a[3]
s += a[5]
print(s[::-1])
