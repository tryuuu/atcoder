H,W=map(int,input().split())
S=[list(input())for _ in range(H)]

def dfs_non_recursive(i, j, S, visited):
    H, W = len(S), len(S[0])
    stack = [(i, j)]
    
    while stack:
        x, y = stack.pop()
        
        if x < 0 or x >= H or y < 0 or y >= W or visited[x][y] or S[x][y] == ".":
            continue
        
        visited[x][y] = True
        
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                stack.append((x + dx, y + dy))

def solver(S):
    H, W = len(S), len(S[0])
    visited = [[False] * W for _ in range(H)]
    count = 0

    for i in range(H):
        for j in range(W):
            if not visited[i][j] and S[i][j] == "#":
                count += 1
                dfs_non_recursive(i, j, S, visited)

    return count

print(solver(S))