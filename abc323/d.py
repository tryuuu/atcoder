def min_slimes(N, S, C):
    MAXN = 1 << N
    dp = [float('inf')] * MAXN
    dp[0] = 0

    # Calculate the total number of slimes for each state
    total_slimes = [0] * MAXN
    for mask in range(MAXN):
        for i in range(N):
            if mask & (1 << i):
                total_slimes[mask] += C[i]

    for mask in range(MAXN):
        for i in range(N):
            # If the size Si exists in the current state
            if mask & (1 << i):
                # We can merge slimes of size Si if we have more than one of them
                num_slimes = total_slimes[mask] - C[i]
                if num_slimes >= C[i]:
                    # Calculate the new state after merging slimes of size Si
                    new_size = 2 * S[i]
                    new_mask = mask
                    if new_size in S:
                        idx = S.index(new_size)
                        new_mask |= (1 << idx)
                    dp[new_mask] = min(dp[new_mask], dp[mask] + num_slimes - C[i] + 1)

                # We can also keep the slimes of size Si as they are
                dp[mask] = min(dp[mask], dp[mask ^ (1 << i)] + C[i])

    return dp[MAXN - 1]

# テスト
N = int(input())
S = []
C = []
for _ in range(N):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)
print(min_slimes(N, S, C))  # この例では答えは3となります。
