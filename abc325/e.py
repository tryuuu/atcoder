N, A, B, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(N)]

# DPテーブルの初期化
dp = [[float('inf')] * 2 for _ in range(N)]
dp[0][0] = 0
dp[0][1] = A * D[0][N-1]

# DPテーブルの更新
for i in range(1, N):
    # 社用車を使って移動する場合
    dp[i][0] = min(dp[i][0], dp[i-1][0] + A * D[i-1][i])
    dp[i][0] = min(dp[i][0], dp[i-1][1] + A * D[i-1][i])

    # 電車を使って移動する場合
    dp[i][1] = min(dp[i][1], dp[i-1][0] + B * D[i-1][i] + C)
    dp[i][1] = min(dp[i][1], dp[i-1][1] + B * D[i-1][i])

# 最短時間を求める
min_time = min(dp[N-1][0], dp[N-1][1])
print(min_time)
