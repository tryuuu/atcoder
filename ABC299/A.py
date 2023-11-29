N=int(input())
s=input()
for i in range(N):
    idx1=s.index('|')
    idx2=s.index('|',idx1+1)
    idx3=s.index('*')
if idx1<idx3<idx2:
    print("in")
else:
    print("out")