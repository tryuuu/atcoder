from collections import defaultdict
import sys
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sys.setrecursionlimit(10**6)

def check(graph, node, color):
    for neighbor in graph[node]:
        if neighbor in color:
            if color[neighbor] == color[node]:
                return False
        else:
            color[neighbor] = 1 - color[node]
            if not check(graph, neighbor, color):
                return False
    return True

def find(A, B, N, M):
    graph = defaultdict(list)
    color = {}

    for i in range(M):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])

    for node in range(1, N+1):
        if node not in color:
            color[node] = 0
            if not check(graph, node, color):
                return "No"

    return "Yes"

print(find(A,B,N,M))
