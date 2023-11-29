N,T=map(int,input().split())
c=list(map(int,input().split()))
r=list(map(int,input().split()))
maxa=-1
flag=0
for i in range(N):
    if(c[i]==T):
        flag+=1
        break
if flag==1:
    for i in range(N):
        if c[i]==T:
            if maxa<r[i]:
                maxa=r[i]
                result=i+1
    print(result)
    exit()
maxa=-1
if flag==0:
    for i in range(N):
        if c[0]==c[i]:
            if maxa<r[i]:
                maxa=r[i]
                result=i+1
    print(result)
    exit()

