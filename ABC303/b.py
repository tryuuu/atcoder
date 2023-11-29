N,M=map(int,input().split())
a = [list(map(int,input().split())) for _ in range(M)]
b = [set() for _ in range(N+1)]
for i in range(len(a)):
    for j in range(len(a[i])):
        if j==0:
            b[a[i][j]].add(a[i][j+1])
        elif j==len(a[i])-1:
            b[a[i][j]].add(a[i][j-1])
        else:
             b[a[i][j]].add(a[i][j+1])
             b[a[i][j]].add(a[i][j-1])

count=0
for i in range(1,N+1):
    for j in range(1,N+1):
        if j not in b[i]:
            count+=1
print((count-N)//2)






        

