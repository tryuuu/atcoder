D=int(input())
import math

def solver(D):
    min_diff = float('inf')
    x = 0
    y = int(math.sqrt(D))
    #xは0から√Dになるまで全探索、yは√Dから始めてxに応じて値を減らしていく
    while x <= y:
        diff = abs(x**2 + y**2 - D)
        if diff < min_diff:
            min_diff = diff

        if x**2 + y**2 < D:
            x += 1
        else:
            y -= 1

    return min_diff
print(solver(D))