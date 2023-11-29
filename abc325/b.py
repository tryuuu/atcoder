N=int(input())
W=[0 for _ in range(N)]
S=[0 for _ in range(N)]
data = []
for _ in range(N):
    w,s=map(int,input().split())
    W.append(w)
    S.append(s)
    data.append((w,s))
data.sort(key=lambda x: x[0], reverse=True)
count=0
data2=[]
for i in range(25):
    result=0
    for item in data:
        time=item[1]+i
        if time>=24:
            time-=24
        if time>=9 and time<=17:
            result += item[0]
    data2.append((result,i))
data2.sort(key=lambda x: x[0], reverse=True)
for item in data2:
    print(item[0])
    break
    
