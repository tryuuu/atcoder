N = int(input())
a = list(map(int, input().split()))
b=[0]*len(a)
if len(a) == len(set(a)):
    print("Yes")
else:
    j=0
    a.sort(reverse=True)
    for i in range(len(a)):
        if i%2==1:
            b[i]=a[j]
            j+=1
    for i in range(len(a)):
        if i%2==0:
            b[i]=a[j]
            j+=1
    for i in range(len(b)):
        if i%2==1:
            if b[i]>b[i-1] and b[i]>b[i+1]:
                continue
            else:
                print("No")
                exit()
    print("Yes")
#ARC初AC!
    