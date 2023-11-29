H,W=map(int,input().split())
#行列Aは一次元のリストが行の分だけ集まってできていると考える
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]

def is_shift_match(A, B):
    H, W = len(A), len(A[0])
    for i in range(H):
        for j in range(W):
            #A[i:]はi行目以降を取り出す(iは0から)
            #A[:i]は最初のi行を取り出す
            #Aは一次元リストの集まりと捉える
            shifted_A = A[i:] + A[:i]#縦シフト,iであることに注意
            #行列の各行について処理
            shifted_A = [row[j:] + row[:j] for row in shifted_A]#横シフト,jであることに注意
            #これと同じ
            '''for i in range(len(shifted_A)):#len(shifted_A)はshifted_Aの行の数
                    row = shifted_A[i]#i行目
                    shifted_A[i] = row[j:] + row[:j]#i行目のリストをjだけシフト
            '''
            if shifted_A == B:
                return True
    return False
if is_shift_match(A, B):
    print("Yes")
else:
    print("No")
