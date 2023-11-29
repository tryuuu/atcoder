N,L,R=map(int,input().split())
A=list(map(int,input().split()))
def solver(A, L, R):
    answer = []

    for a in A:
        if L <= a <= R:
            answer.append(a)
        elif a < L:
            answer.append(L)
        else:
            answer.append(R)
    
    return answer
a=solver(A,L,R)
a=' '.join(map(str, a))
print(a)