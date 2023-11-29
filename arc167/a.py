N, M = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
result=0

def makeset(N,M):
    A=[1]*M
    diff=N-M
    for i in range(diff):
        A[i]+=1
    return A
j=0
result=0
B=makeset(N,M)
i = 0
num=0
for i in range(len(B)):
    if B[i]==2:
        num+=1
    else:
        break
i=0
j=0
z=0
flag=True
while i < N:
    if j<len(B) and B[j] == 2:
        sum_val = A[i] + A[num*2-1-z]
        z+=1
        result += sum_val * sum_val
        j += 1
        i += 1
    elif j>=len(B):
        resul=result*result
        break
    else:
        if flag:
            i=i*2
            flag=False
        sum_val = A[i]
        result += sum_val * sum_val
        i += 1  
print(result)



