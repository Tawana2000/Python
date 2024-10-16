#write a python function to return the summetric difference of two sets

def sym(set1, set2):
    
    result  = set(set1) ^ set(set2)
    
    return set(sorted(result))

set1 = input().split()
set2 = input().split()
print(sym(set1,set2))