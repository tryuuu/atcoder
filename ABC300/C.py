H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

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
#result[0](サイズが0)は不要より一つ増やす
result=[0]*(N+1)
for i in range(H):
    for j in range(W):
        if C[i][j]=='#':
        #resultリストのindexはサイズ、値(key)はその個数
            result[check(i,j)]+=1
#result[0]はいらない
print(*result[1:])
'''list = [1, 2, 3]というリストがある場合、print(*list)と書くと、
print(1, 2, 3)と同じように展開され、3つの引数が渡される'''