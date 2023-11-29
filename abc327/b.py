B=int(input())
import math

def find(B):
    if B == 1:
        return 1
    lower = 1
    upper = int(math.log(B, 2)) + 1 
    while lower <= upper:
        mid = (lower + upper) // 2
        power = mid**mid
        if power == B:
            return mid
        elif power < B:
            lower = mid + 1
        else:
            upper = mid - 1
    
    return -1
a=find(B)
print(a)