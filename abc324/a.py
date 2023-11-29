N=int(input())
A=list(map(int,input().split()))
def solver(lst):
    return "Yes" if len(set(lst)) == 1 else "No"
print(solver(A))
