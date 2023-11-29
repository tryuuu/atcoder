N,M=map(int,input().split())
A=list(map(int,input().split()))
A=sorted(A)
def solver(N, M, A):
    start, end = 0, 0
    max_presents = 0
    
    while end < N:
        while end < N and A[end] - A[start] < M:
            end += 1
        max_presents = max(max_presents, end - start)
        
        start += 1
    
    return max_presents

print(solver(N,M,A))