n,m = map(int,input().split())
s=input()
t=input()

def checker(N, M, S, T):
    is_prefix = (S == T[:N])
    is_suffix = (S == T[M-N:])
    
    if is_prefix and is_suffix:
        return 0
    elif is_prefix:
        return 1
    elif is_suffix:
        return 2
    else:
        return 3

print(checker(n,m,s,t))
