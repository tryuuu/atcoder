N=int(input())#キャスト忘れずに
A=list(map(int,input().split()))
Q=int(input())
B=[int(input()) for _ in range(Q)]
A=sorted(A)
result=[]
for i in range(Q):
    left=0
    right=N-1
    while right-left>1:
        mid=(left+right)//2
        if B[i]<A[mid]:
            right=mid
        else:
            left=mid
    if left==N-1:
        result.append(abs(B[i]-A[N-1]))
    elif right==0:
        result.append(abs(A[0]-B[i]))
    else:
        result.append(min(abs(B[i]-A[right]),abs(B[i]-A[left])))
for i in range(len(result)):
    print(result[i])


