H, W = map(int, input().split())
S = [[] for _ in range(H)]
for i in range(H):
    S[i] = input()

def check_s(i, j):
    if S[i][j] == "s":
        return True

def check_n(i, j):
    if S[i][j] == "n":
        return True

def check_u(i, j):
    if S[i][j] == "u":
        return True

def check_k(i, j):
    if S[i][j] == "k":
        return True

def check_e(i, j):
    if S[i][j] == "e":
        return True

for i in range(H):
    for j in range(W):
        if check_s(i, j):
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if 0 <= i + 4 * a < H and 0 <= j + 4 * b < W:  # インデックスの範囲をチェック
                        if check_n(i + a, j + b) and check_u(i + 2 * a, j + 2 * b) and check_k(i + 3 * a, j + 3 * b) and check_e(i + 4 * a, j + 4 * b):
                            print(i+1, j+1)
                            print(i+1+a, j+1+b)
                            print(i+1+a*2, j+1+b*2)
                            print(i+1+a*3, j+1+b*3)
                            print(i+1+a*4, j+1+b*4)

                            exit()

