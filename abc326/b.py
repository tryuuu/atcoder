N=int(input())
def solver(N):
    while True:
        hundreds = N // 100
        tens = (N % 100) // 10
        units = N % 10
        
        if hundreds * tens == units:
            return N
        N += 1
print(solver(N))
