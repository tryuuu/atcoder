n,x=map(int,input().split())
a = list(map(int, input().split()))
a = sorted(a)
sum1 = 0
sum2 = 0
sum3 = 0
min = a[0]
max = a[len(a)-1]

for i in range(len(a)-1):
    sum1 += a[i]
for i in range(1,len(a)):
    sum2 += a[i]
for i in range(1,len(a)-1):
    sum3 += a[i]
if len(a)==2:
    if a[0]>=x:
        print("0")
    elif a[0]<=x and a[1]>=x:
        print(x)
    else:
        print("-1")
elif x<=sum1:
    print("0")
elif (x-sum3)>=min and (x-sum3)<=max:
    print(x-sum3)

elif x==sum2:
    print(max)
else:
    print("-1")