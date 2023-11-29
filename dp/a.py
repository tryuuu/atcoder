N=int(input())
h=list(map(int,input().split()))
dp=[0]*N
for i in range(N):
    if i==0:
        continue
    elif i==1:
        dp[i]+=dp[i-1]+abs(h[i]-h[i-1])
    else:
        diff=abs(h[i]-h[i-1])
        diff2=abs(h[i]-h[i-2])
        dp[i]+=min(dp[i-2]+diff2,dp[i-1]+diff)
print(dp[N-1])
