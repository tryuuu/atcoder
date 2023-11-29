import itertools
import math

def count_square_numbers(S: str) -> int:
    # Generate all permutations of S
    permutations = set(itertools.permutations(S))
    
    count = 0
    for perm in permutations:
        # Convert tuple to string
        num_str = ''.join(perm)
        
        # Ignore numbers starting with '0'
        if num_str[0] == '0':
            continue
        
        # Convert string to integer
        num = int(num_str)
        
        # Check if the number is a perfect square
        if math.isqrt(num)**2 == num:
            count += 1
            
    return count

N=int(input())
S=input()
a=count_square_numbers(S)
print(a)
