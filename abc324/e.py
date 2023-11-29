from collections import deque

def min_path_length(N, A, Q, queries):
    # 隣接行列の初期化
    graph = [[0] * (N * N) for _ in range(N * N)]
    
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                for u in range(N):
                    for v in range(N):
                        graph[u * N + i][v * N + j] = 1
    
    def bfs(s, t):
        if s == t:
            return 0
        visited = [False] * (N * N)
        queue = deque([(s, 0)])
        visited[s] = True
        
        while queue:
            node, dist = queue.popleft()
            row, col = divmod(node, N)
            for v in range(N * N):
                if graph[node][v] == 1 and not visited[v]:
                    visited[v] = True
                    if v == t:
                        return dist + 1
                    queue.append((v, dist + 1))
        return -1  # 経路が存在しない場合
    
    results = []
    for s, t in queries:
        s_mod_N = s % N
        t_mod_N = t % N
        if s_mod_N == t_mod_N:
            results.append(-1)
        else:
            results.append(bfs(s, t))
    
    return results

# 入力例
N = 3
K = 2
A = [
    [1, 1, 1],
    [1, 1, 0],
    [0, 1, 0]
]
Q = 2
queries = [(1, 2), (3, 6)]

results = min_path_length(N, A, Q, queries)
for result in results:
    print(result)
