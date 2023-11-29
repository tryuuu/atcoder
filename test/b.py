N,M=map(int,input().split())
E=[[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
  a,b,c=map(int,input().split())
  E[a][b]=c
  E[b][a]=c

ans=0
#「その点は通っていない」で初期化
used=[False]*(N+1)

def dfs(v,s):
  global ans
  #点v空の距離の最大値を探している間は使用済みにしておく(同じ道を通らないように)
  used[v]=True
  #最大値(の候補を)を更新していく
  if s>ans: ans=s
  for i in range(1,N+1):
    #その点はまだ通っておらず、かつ道が存在する場合
    if not used[i] and E[v][i]:
      dfs(i,s+E[v][i])
  used[v]=False

for i in range(1,N+1):
  dfs(i,0)

print(ans)
