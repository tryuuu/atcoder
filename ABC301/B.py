N=int(input())
A=list(map(int,input().split()))

def insert(a, b):
     c = []
     if a < b:
          for i in range(b - a-1):
               c.append(a + i+1)
     elif b < a:
          for i in range(a - b-1):
               c.append(a - i-1)
     return c
B=A.copy()
x=0
for i in range(len(A)):
    if i!=len(A)-1:
        if i==0:
            B[i+1:i+1]=insert(A[i],A[i+1])
        else:
         x+=len(insert(A[i-1],A[i]))
         B[i+1+x:i+1+x]=insert(A[i],A[i+1])
print(*B)


