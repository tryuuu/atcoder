def checker(s):
    flag = True
    for i in range(2, 17, 2): 
        if s[i-1] == '0':  
            continue
        else:
            flag = False
    return flag
S=input()
if checker(S):
    print("Yes")
else:
    print("No")