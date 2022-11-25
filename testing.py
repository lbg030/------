from sys import stdin
acc = []
f1 = []
cnt = 0
f_a = []
f_f = []

for _ in range(60):
    a, b = stdin.readline().rstrip().split(" : ")
    
    if a.startswith("acc"):
        acc.append(float(b))
    else :
        f1.append(float(b))
    cnt += 1
    
    if cnt == 20:
        cnt = 0
        f_a.append(acc)
        f_f.append(f1)
        
        acc = []
        f1 = []
        

acc = []
f1 = []

for i in range(10):
    f1_s = 0
    acc_s = 0
    
    for j in range(3):
        f1_s += f_f[j][i]
        acc_s += f_a[j][i]
    
    acc.append(round(acc_s/3 , 5))
    f1.append(round(f1_s/3 , 5))
    
print(acc)
print(f1)