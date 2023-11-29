"""方針は、
①二分探索により候補を探していく(最大を探せる)
②それぞれの候補が条件を満たすかcheck"""
#計算量はO(NlogN)
#二分探索は、候補のうちYesとNGの間を出すことができる
#最小値の最大化を知りたいときに有用
N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]

def is_ok(l):
    n = 0
    prev = 0
    for i in range(1, len(A)):
        if A[i] - prev >= l:
            n += 1
            prev = A[i]
    if n >= K + 1:
        return True
    else:
        return False

left = 0
right = L
#最後はrightとleftが隣り合う
while right - left > 1:
    mid = (left + right) // 2
    #ギリギリまで大きくする
    if is_ok(mid):
        left = mid
    #大きすぎたので減らす
    else:
        right = mid

print(left)
