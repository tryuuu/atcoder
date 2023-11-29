S=input()
T=input()
s=['a','t','c','o','d','e','r']

def make_dict(x):
    dict1={}
    for word in x:
        for char in word:
            if char in dict1:
                dict1[char]+=1
            else:
                dict1[char]=1
    return dict1

dict2=make_dict(S)
dict3=make_dict(T)


