H,W=map(int,input().split())
S=[list(input())for _ in range(H)]
visited=[[False] * W for _ in range(H)]

def checker(a,b):
    if a<0 or b<0 or a>H-1 or b>W-1:
        return False
    else:
        return True

def dfs(a,b):
    stack=[(a,b)]
    while stack:
        #stackはLIFO
        a,b=stack.pop()
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if checker(a+i,b+j) and S[a+i][b+j]=='#' and not visited[a+i][b+j]:
                    visited[a+i][b+j]=True
                    stack.append((a+i,b+j))

def solver():
    count=0
    for i in range(H):
        for j in range(W):
            if S[i][j]=='#' and not visited[i][j]:
                count+=1
                dfs(i,j)
    print(count)
solver()

