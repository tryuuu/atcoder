N=int(input())
S=input()

def check(S):
    if 'ab' in S or 'ba' in S:
        return 'Yes'
    else:
        return 'No'
a=check(S)
print(a)