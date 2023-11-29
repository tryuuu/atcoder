N, T = input().split()
N = int(N)
S=[]
for _ in range(N):
    s=input()
    S.append(s)
def levenshtein_distance(S, T):
    INSERT_COST = 1
    DELETE_COST = 1
    CHANGE_COST = 1

    sl = len(S)
    tl = len(T)

    dp = [[0 for _ in range(tl+1)] for _ in range(sl+1)]

    for i in range(sl+1):
        dp[i][0] = i * INSERT_COST
    for j in range(tl+1):
        dp[0][j] = j * INSERT_COST

    for i in range(1, sl+1):
        for j in range(1, tl+1):
            D = dp[i-1][j] + DELETE_COST
            I = dp[i][j-1] + INSERT_COST
            C = dp[i-1][j-1] + (0 if S[i-1] == T[j-1] else CHANGE_COST)
            
            dp[i][j] = min(D, I, C)

    return dp[sl][tl]
count=0
list=[]
for i in range(N):
     if levenshtein_distance(S[i], T)<=1:
         count+=1
         list.append(i+1)
output = " ".join(map(str, list))
print(count)
print(output)


