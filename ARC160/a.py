import copy
N, K = map(int, input().split())
A = list(map(int, input().split()))
C = [[] for _ in range(N * (N + 1) // 2)]
A2=sorted(A)

def rev(a, b):
    B = []
    j = 0
    for i in range(N):
        if i not in range(a-1, b):
            B.append(A[i])
        else:
            B.append(A[b-1-j])
            j += 1
    return B

def form(p):
    if p == sorted(p):
        return p
    li = []
    while True:
        x = p.pop(-1)
        li.append(x)
        if min(li) != x:
            li.sort()
            i = li.index(x)
            p.append(li.pop(i-1))
            break
    for i in range(1, len(li)+1):
        p.append(li[-i])
    return p

def countfunc(c,count=0):
    memo=["None"]*N
    if A2 == c:
        return count
    elif 
    if A2 != c:
        count+=1
        c=form(c)
        return countfunc(c,count)

k = 0
for i in range(N):
    for j in range(i+1, N+1):
        C[k] = rev(i+1, j).copy()
        k += 1
n=(N * (N + 1) // 2)
D=[0]*n
C_copy=copy.deepcopy(C)
for i in range(len(C)):
    value=countfunc(C[i])
    D[i]=value
#countfuncnの値をDにappebdするcountfuncは0となる
E=D.copy()
E=sorted(E)
C_copy2=copy.deepcopy(C_copy)
for i in range(len(C)):
    if countfunc(C_copy[i])==E[k-1]:
        print(*C_copy2[i])

#E[k-1]のCを出力




    









        





