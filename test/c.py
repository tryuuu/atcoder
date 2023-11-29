N,M = map(int,input().split())
G = [[0]*(N+1) for _ in range(N+1)]
g = [[False]*(N+1) for _ in range(N+1)]
for _ in range(M):
    A,B,C = map(int,input().split())
    G[A][B] = C
    G[B][A] = C

def get_max(v):
    score = 0
    for i in range(1,N+1):
        if score < G[v][i] and (g[v][i] == False or g[i][v] == False):
            score = G[v][i]
    for i in range(1,N+1):
        if score == G[v][i]:
            g[v][i] = True
            g[i][v] = True
    return score



score = 0
for i in range(1,N+1):
    score += get_max(i)

print(score)
#このコードは、「各点について隣の点までの距離が最大の道」を集めているが、必ずしもそれを集めることで合計の道のりが最大になるとは限らない