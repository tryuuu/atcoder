N,M=map(int,input().split())
#こうすると、a[0]で一つのリスト
#a=[list(map(int,input().split()))]
#これで正しく入力される
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=A+B
C=sorted(C)
#for 変数1,変数2 in enumerate(リスト等の変数):
#enumerate()関数を使ってリストCをループし、各要素とそのインデックスを取得
#enumerate()関数の戻り値は、(index, element)のタプル(順番注意)
#get_indexの引数はリストの要素
#iがindex
#cはリストの要素
#i+1が答え
#リストC内の各要素に対応する(index+1)がget_indexに格納
get_index = {c: i + 1 for i, c in enumerate(C)}#辞書を作成
for a in A:
    print(get_index[a],end=' ')
print()
for b in B:
    print(get_index[b],end=' ')