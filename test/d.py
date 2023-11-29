#幅優先探索: 全探索を行う
N,M = map(int,input().split())
G = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    A,B,C = map(int,input().split())
    G[A][B] = C
    G[B][A] = C
max = 0
used = [False]*(N+1)#同じ点は一回しか通れないので

#点iをスタート地点とした時の結果を保持しながら更新
def dfs(v,score):
    #点vをスタート地点とした場合vは使用済みに((スタート地点: 毎回更新)は通らないように)
    used[v] = True
    global max
    #最大値を超えた時点で更新(超えても処理は変わらず継続)
    if score > max:
        max = score
    for i in range(1,N+1):
        #点vからの道がある点があれば、そこをスタート地点として再帰
        #1回通った点は使用できない
        if G[v][i] and not used[v]:
            score += G[v][i]
            dfs(i,score)
    used[v] = False
    
##どこをスタート地点としたら(score)最も大きく(max)なるか
for i in range(1,N+1):
    #初めのscoreは0
    dfs(i,0)
print(max)