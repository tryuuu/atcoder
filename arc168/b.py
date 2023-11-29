def game_outcome(N, K, a):
    # DPテーブルの初期化（PythonではFalseで初期化される）
    dp = [False] * (K + 1)

    # DP
    for i in range(1, K + 1):
        for j in range(N):
            if i - a[j] >= 0:
                #dp[i-a[j]]がFalseなら相手が詰むので自分がTrue
                #dp[i]は一度TrueになればずっとTrue
                dp[i] |= not dp[i - a[j]]

    # 勝者の判定
    if dp[K]:
        return "First"
    else:
        return "Second"

# 入力
N, K = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)

# 結果の出力
print(game_outcome(N, K, a))
