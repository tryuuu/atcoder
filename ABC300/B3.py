H,W=map(int,input().split())
A=[list(input()) for _ in range(H)]
B=[list(input()) for _ in range(H)]

def shift():
    for i in range(H):
        for j in range(W):
            C=A[i:]+A[:i]#+でリストの結合が可能,縦シフト
            for k in range(len(C)):
                row=C[k]
                C[k]=row[j:]+row[:j]#1行ずつ処理して横シフトを完成
            if B==C:
                return True
    return False

if shift():
    print("Yes")
else:
    print("No")


