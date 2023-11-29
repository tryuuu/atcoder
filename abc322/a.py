n = int(input())
s = input()

def checker(n, s):
    for i in range(n - 2): 
        substring = s[i:i+3]
        if substring == 'ABC':
            return i + 1
    return -1

print(checker(n,s))
