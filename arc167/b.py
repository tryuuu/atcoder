A,B=map(int,input().split())
def is_prime(N):
    if N <= 1:
        return False
    if N <= 3:
        return True
    if N % 2 == 0 or N % 3 == 0:
        return False
    i = 5
    while i * i <= N:
        if N % i == 0 or N % (i + 2) == 0:
            return False
        i += 6
    return True

def makesum(n):
    return n*(n+1)/2
if is_prime(A):
    print(int(makesum(B)))
else:
    print("a")