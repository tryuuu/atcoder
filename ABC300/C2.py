H,W=map(int,input().split())
C=[list(input()) for _ in range(H)]

def check(i, j):
    n = 0
    while True:
        _n = n + 1
        #バツの真ん中であればok,nがサイズ,中央から広がるイメージ
        if not (i + _n < H and j + _n < W and C[i + _n][j + _n] == '#'):
            break
        if not (i + _n < H and j - _n >= 0 and C[i + _n][j - _n] == '#'):
            break
        if not (i - _n >= 0 and j + _n < W and C[i - _n][j + _n] == '#'):
            break
        if not (i - _n >= 0 and j - _n >= 0 and C[i - _n][j - _n] == '#'):
            break
        n += 1

    return n

N=min(H,W)
result=[0]*(N+1)
for i in range(H):
    for j in range(W):
        if C[i][j]=='#':
            result[check(i,j)]+=1
print(*result[1:])

