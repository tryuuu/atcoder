import math

def check(N, positions, D):
    #True:感染
    infected = [False] * N 
    infected[0] = True
    queue = [0]  
    #queueが空になるまで
    while queue:
        #queueの先頭を取り出す(その要素は削除される)
        current = queue.pop(0)
        x1, y1 = positions[current]
        #x_currentが感染している時感染する人をqueueに追加
        for i in range(N):
            #Falseの時
            if not infected[i]:
                x2, y2 = positions[i]
                distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if distance <= D:
                    infected[i] = True
                    #感染している人をqueueに追加
                    queue.append(i)

    return infected
#リストを返す

N, D = map(int, input().split())  
positions = []
for _ in range(N):
    x, y = map(int, input().split())
    positions.append((x, y))

result = check(N, positions, D)
#返された各リストの要素について
for i in result:
    if i:
        print("Yes")
    else:
        print("No")
