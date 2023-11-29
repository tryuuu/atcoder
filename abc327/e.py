N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
mix = list(zip(A,B))
mix = sorted(mix,key=lambda x:x[0])
A,B=zip(*mix)

def find():
    X = [0]*N
    visited = [False]*N
    for i in range(M):
        if visited[A[i]-1] is False and visited[B[i]-1] is False:
            X[A[i]-1] = 0
            X[B[i]-1] = 1
            visited[A[i]-1] = True
            visited[B[i]-1] = True
        if visited[A[i]-1] is False and visited[B[i]-1] is True:
            if X[B[i]-1] == 0:
                X[A[i]-1] = 1
            else:
                X[A[i]-1] = 0
                visited[A[i]-1] = True
        if visited[A[i]-1] is True and visited[B[i]-1] is False:
            if X[A[i]-1] == 0:
                X[B[i]-1] = 1
            else:
                X[B[i]-1] = 0
                visited[B[i]-1] = True
        else:
            if X[A[i]-1] != X[B[i]-1]:
                continue
            else:
                return "No"
    return "Yes"
a=find()
print(a)
#コーナーケース:
#既に訪れたノードへの追加のリンク（例：A=[1,2,1], B=[2,3,3]）