"""幅優先、深さ優先について
https://zero2one.jp/learningblog/breadth-first-depth-first-search/"""
"""1からの距離を求め、最も遠い場所を見つけ、(DFSで)その場所からの距離を計算することで、
新しい道路を追加することスコアの最大値を得る"""
#Gは隣接リスト
#distは各頂点からの距離を表す
N=int(input())
G=[[] for _ in range(N+1)]#N+1個のリストを初期化
for _ in range(N-1):
    a,b=map(int,input().split())
    #aに隣接する頂点を追加していく(G[a]は複数ある場合がある)
    G[a].append(b)
    G[b].append(a)#Gは頂点iに隣接する頂点が格納

dist=[-1]*(N+1)#-1で初期化,l
dist[1]=0#頂点1からスタートするため

#引数一つならlastはデフォルトで-1となる
def dfs(now,last=-1):
    #nxtはnowの隣接頂点。初めなら1の隣の頂点
    #G[now]は隣接頂点を格納したリストなので複数ある可能性がある
    for nxt in G[now]:
        #次の頂点と前の頂点が同じとき
        #戻り道を進むのを避けている
        if nxt==last:
            continue
        dist[nxt]=dist[now]+1
        dfs(nxt,now)#再帰

flag=True
#1周目は最も遠いノードを見つける
#2周目はそのノードを根として再度深さ優先探索
for _ in range(2):
    dist=[-1]*(N+1)
    #1周目
    if flag:
        dist[1]=0
        dfs(1)#頂点1からスタート
        tmp=max(dist)
        idx=dist.index(tmp)
    else:
        #1から最も遠い所から再スタート
        dist[idx]=0
        dfs(idx)
        print(max(dist)+1)


