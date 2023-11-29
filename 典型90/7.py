from bisect import bisect, bisect_left
N=int(input())#キャスト忘れずに
A=list(map(int,input().split()))
Q=int(input())
B=[int(input()) for _ in range(Q)]
A=sorted(A)
result=[]
for i in range(Q):
    pos=bisect_left(A,B[i])#二分探索
    if pos==N:
        result.append(B[i]-A[N-1])#リストに要素を加えるときはappendで
    elif pos==0:
        result.append(A[0]-B[i])
    else:
        result.append(min(abs(B[i]-A[pos]),abs(B[i]-A[pos-1])))
for i in range(len(result)):
    print(result[i])
