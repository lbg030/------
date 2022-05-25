case = int(input())
#(100+1+ | 01)+
lst = [['1','0','1'], ['0','1']]
for i in range(case):
    compared = input()
    queue = []
    
    # set해서 101 or 01이 되면 
    queue.append(compared[0])
    for x in compared:
        if queue :
            if x != queue[-1] :
                queue.append(x)
        else :
            queue.append(x)
            
        
        if queue[:2] in lst :
            queue = queue[2:]
        elif queue[:3] in lst:
            queue = queue[3:]
            
        print(queue)
    if queue :
        print("NO")
    else :
        print("YES")