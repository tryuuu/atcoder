n=int(input())
s=[list(input())for _ in range(n)]

def checker(N, results):
    wins = [row.count('o') for row in results]
    rankings = [(wins[i], i+1) for i in range(N)]
    sorted_rankings = sorted(rankings, key=lambda x: (-x[0], x[1]))
    return [player_num for _, player_num in sorted_rankings]

result = []
result = checker(n, s)
answer = " ".join(map(str, result))
print(answer)