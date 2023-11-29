w,h = map(int,input().split())
n = int(input())
p = []
q = []
for i in range(n):
    pq = list(map(int,input().split()))
    p.append(pq[0])
    q.append(pq[1])
na = int(input())
a = list(map(int,input().split()))
nb = int(input())
b = list(map(int,input().split()))

import bisect
d = dict()
for i in range(n):
    pp = bisect.bisect(a,p[i])
    qq = bisect.bisect(b,q[i])
    if (pp,qq) not in d:
        d[(pp,qq)] = 1
    else:
        d[(pp,qq)] += 1
print(d)
c=[d[i] for i in d]
print(c)