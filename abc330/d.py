N=int(input())
S=[]
for _ in range(N):
    S.append(list(input()))

def solver(N, grid):
    count = 0
    row = [0] * N
    col = [0] * N
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'o':
                row[i] += 1
                col[j] += 1
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'o':
                count += (row[i] - 1) * (col[j] - 1)

    return count
print(solver(N,S))