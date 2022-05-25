case = int(input())
#(100+1+ | 01)+
lst = ['101','01']

def overlap(a):
    string = ''
    for x in a:
        if string:
            if string[-1] != x:
                string += x
        else :
            string += x
    
    return string

for i in range(case):
    compared = input()
    queue = ''
    queue2 = ''
    # set해서 101 or 01이 되면 
    for x in compared:
        if not queue:
            queue += x
        
        else :
            if queue == '01':
                queue =''
                queue += x
            elif queue == '100':
               if x == '1':
                    queue += x
            elif queue == '1001':
                if x == '0':
                    queue = '0'
            else:
                queue += x
    # print(queue)
    if queue in lst:
        print("YES")
    else :
        if queue:
            # print(len(queue), queue[:3])
            if len(queue) < 4 or queue[:3] == 100:
                # print("??")
                print("NO")
            else:
                a = overlap(queue)
                # print(a)
                if a in lst:
                    print("YES")
                else:
                    print("NO")
        else:
            print("YES")
