from collections import deque

tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], [], [], [], [], []]

queue = deque([0])
while queue:
    now = queue.popleft()
    print(now)
    for i in tree[now]:
        queue.append(i)
