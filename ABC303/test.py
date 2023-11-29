N=10
a=set()
b=[set() for _ in range(N+1)]
for i in range(3):
    xi, yi = map(int, input().split())
    a.add((xi, yi))
    b[i].add((xi, yi))
print(a)
print(b)