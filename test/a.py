N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F_sorted = sorted(F)
F_last = []
score = 0
count = 0
j = 0
for i in range(1, N):
    n = len(F_sorted)-1
    if (n+1)<D:
        F_last = F_sorted
    else:
        F_last = F_sorted[-D:]
    #print(F_last)
    #print(F_sorted)
    if sum(F_last) > P and count < D:
        score += P
        count += 1
        n = len(F_sorted)-1-D
        if n < 0:
            break
    else:
        score += sum(F_sorted)
        break
    F_sorted = F_sorted[:-D]
print(score)
    