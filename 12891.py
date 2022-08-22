# A C G T
from itertools import permutations

n , m =map(int, input().split())
string = input()
DNA_List = ['A', 'C','G','T']
Minimum_DNA_Count_list = list(map(int, input().split()))
comb_string_list = []
comb_set = set()
def check():
    for i in range(4):
        if (Minimum_DNA_Count_list[i]) != 0  and string.count(DNA_List[i]) < (Minimum_DNA_Count_list[i]):
            print(i)
            print('12')
            return False
        else :
            for k in range((Minimum_DNA_Count_list[i])):
                comb_string_list.append(DNA_List[i])
    return True

if not check():
    print("0")
    
else :
    needs = sum(Minimum_DNA_Count_list)
    rest = m - needs
    lst = set(permutations(comb_string_list, len(comb_string_list)))