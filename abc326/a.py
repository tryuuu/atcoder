X,Y=map(int,input().split())
if X<Y:
    n=Y-X
    if n>2:
        print("No")
    else:
        print("Yes")
else:
    n=X-Y
    if n>3:
        print("No")
    else:
        print("Yes")