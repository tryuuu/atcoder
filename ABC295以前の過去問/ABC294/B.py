H,W=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(H)]
print(a[0])

for i in range(H):
    for j in range(W):
        if a[i][j]==0:
            a[i][j]='.'
        else:
            a[i][j]=chr(a[i][j]+64)##ascii codeを文字列に変換
for i in range(H):
    print("".join(a[i]))

