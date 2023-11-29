N=int(input())
a=[[0 for _ in range(3)] for _ in range(N)]
for i in range(N):
    a1=list(map(int, input().split()))
    for j in range(3):
        a[i][j]=a1[j]
dp=[[0 for _ in range(3)] for _ in range(N)]
dp[0][0]=a[0][0]
dp[0][1]=a[0][1]
dp[0][2]=a[0][2]
for i in range(N):
    tmp=0
    if i==0:
        continue
    else:
        for j in range(3):
            max_value = float('-inf')  
            for k in range(3):
                if j != k:
                    max_value = max(max_value, dp[i-1][k] + a[i][j])
            dp[i][j] = max_value  

max=max(dp[N-1][0],dp[N-1][1],dp[N-1][2])
print(max)
    