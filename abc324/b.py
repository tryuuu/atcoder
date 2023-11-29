N=int(input())
def solver(N):
    while N % 2 == 0 and N > 1:
        N //= 2

    while N % 3 == 0 and N > 1:
        N //= 3
    if N == 1:
        return "Yes"
    else:
        return "No"
print(solver(N))