# 転置する配列
a = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9, 10, 11, 12]]

# 配列aの縦と横の大きさ
height = len(a)#3
width = len(a[0])#4

# 配列bを、各要素を0で初期化して定義
b = [[0] * height for _ in range(width)]

# aを転置したものをbに代入
for i in range(height):
    for j in range(width):
        b[j][i] = a[i][j]

# 結果確認
print(b)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 2つの一次元配列を定義する
a = [1, 2, 3]
b = [4, 5, 6]

# 配列同士を足す
c = [x + y for x, y in zip(a, b)]

# 結果を表示する
print(c)  # [5, 7, 9]

# 2つの二次元配列を定義する
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

# 配列同士を足す
c = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

# 結果を表示する
print(c)  # [[6, 8], [10, 12]]
