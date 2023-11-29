#https://www.sejuku.net/blog/21923
n=int(input())
set_strings=set()
for i in range(1,n+1):
    s=input()
    if s in set_strings:
        continue
    print(i)
    set_strings.add(s)
