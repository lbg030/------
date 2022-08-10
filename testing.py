lst = list(input())
lst2 = [lst[i:i+3] for i in range(0,9,3)]

print(lst2)