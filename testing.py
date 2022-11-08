from sys import stdin


f1_list = []
acc_list = []

for i in range(3):
    temp_f1 = []
    temp_acc = []
    for j in range(5):
        k = list(stdin.readline().rstrip().split())
        f1 = (float(k[-1][1:-1]))
        acc = (float(k[-2][1:-1]))

        temp_f1.append(f1)
        temp_acc.append(acc)
        
    f1_list.append(temp_f1)
    acc_list.append(temp_acc)
    
    
mean_f1 = [0,0,0,0,0]
mean_acc = [0,0,0,0,0]
for i in range(3):
    for j in range(5):
        mean_f1[j] += f1_list[i][j]
        mean_acc[j] += acc_list[i][j]
        
