N, A, B = map(int, input().split())
c = list(map(int, input().split()))
sum = A + B
for i in range(N):
    if sum == c[i]:
        print(i + 1)
        exit()
