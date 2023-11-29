H,W=map(int,input().split())
S=[list(input())for _ in range(H)]
counts = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j]==".":
            count=0
            if i>0 and S[i-1][j]=="#":
                count+=1
            if i<H-1 and S[i+1][j]=="#":
                count+=1
            if j>0 and S[i][j-1]=="#":
                count+=1
            if j<W-1 and S[i][j+1]=="#":
                count+=1
            counts[i][j]=count
for i in range(H):
    for j in range(W):
        if counts[i][j]>1:
            print(f"{i+1} {j+1}")


