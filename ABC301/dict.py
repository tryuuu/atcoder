list=['banana','apple','cherry']
#空の辞書を作成
dict={}
for word in list:
    for char in word:
        #辞書にその文字があれば
        if char in dict:
            dict[char]+=1 
            #なければ
        else:
            dict[char]=1
#辞書の中のすべてのキーと値の組み合わせの一覧を取得するには items メソッドを使用
for key,value in dict.items():
    print(key,value)
#b 1
#a 4
#n 2
#p 2
#l 1
#e 2
#c 1
#h 1
#r 2
#y 1