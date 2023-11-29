A=[list(input()) for _ in range(3)]#空白詰めで二次元配列を入力
B=[list(map(int,input().split())) for _ in range(3)]
#B=list(input()) for _ in range(5)#エラー
print(*A)
print(*B)
print(*A,sep='\n')
print(*B,sep='\n')
for a in A:
    print(*a)
for b in B:
    print(*b)
for i in range(len(B[0])):
    for j in range(len(B)):
        print(B[i][j],end='')#''を末尾に加える
        #Pythonではprintだけだと改行されてしまう
    print()#改行
    