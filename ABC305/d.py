import bisect
N=int(input())
A=list(map(int,input().split()))
Q=int(input())
l=[]
r=[]
A2=[]
A3=[]
for i in range(len(A)):
    if i%2==0:
        A2.append(0)
    else:
        A2.append(A[i+1]-A[i])

for i in range(Q):
    L,R=map(int,input().split())
    l.append(L)
    r.append(R)

def funcd(l,r):
    a=bisect.bisect(A,l)
    b=bisect.bisect(A,r)
    if a==b:
        return 0
    else:
        result=0
        if a%2==0:
            result+=A[a]-l
        if b%2==0:
            result+=r-A[b-1]
        A3=A2[a:b-1]
        result+=sum(A3)
    return result

for i in range(Q):
    print(funcd(l[i],r[i]))

 


