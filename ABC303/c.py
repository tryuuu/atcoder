N, M, H, K = map(int, input().split())
S = input()
b = set()

for _ in range(M):
    xi, yi = map(int, input().split())
    b.add((xi, yi))
for element in b:
    print(element)


X = 0
Y = 0
for i in range(N):
    if S[i] == "R":
        X += 1
    elif S[i] == "L":
        X -= 1
    elif S[i] == "U":
        Y += 1
    else:
        Y -= 1

    H -= 1
    if H < 0:
        print("No")
        exit()

    if H < K and (X, Y) in b:
        H = K
        b.remove((X, Y))

print("Yes")
