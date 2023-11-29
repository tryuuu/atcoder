import heapq

N,K = map(int,input().split())
A = list(map(int,input().split()))
B = [0]
heapq.heapify(B)#ヒープ作成
S = set()#重複NG
for _ in range(K):
    n = heapq.heappop(B)#その時の最小の要素を取り出す(Bから消える)
    for a in A:
        if not (n + a in S):
            heapq.heappush(B,n + a)#要素をpush
            S.add(n + a)
print(heapq.heappop(B))#最小値を出力

#方針:heapの中にはSに入っていない新規の要素が入ってきて,popするとその時の最小値が出る(常に変化)
#Sは入ってきた要素を重複なしで管理している