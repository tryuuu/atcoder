N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(list(input()))

count = 0
num = [set() for _ in range(M)]
for j in range(M):
    for i in range(N):
        if S[i][j] not in num[j]:
            count += 1
            num[j].add(S[i][j])
        if i==N-1:
            count-=1
if count < N:
    print("Yes")
else:
    print("No")


        

