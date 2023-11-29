N=int(input())
S=input()
countT=0
countA=0
for i in range(len(S)):
    if S[i]=='T':
        countT+=1
    elif S[i]=='A':
        countA+=1
    a=S[len(S)-1]
if countT<countA:
    print("A")
elif countT>countA:
    print("T")
else:
    if a=='T':
        print("A")
    else:
        print("T")


