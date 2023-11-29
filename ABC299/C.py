N = int(input())
s = input()
b = []
flag = 0
count = 0
for i in range(N):
    if s[i] == "-":
        flag += 1
        continue
    else:
        count += 1
        if i == N - 1 or s[i + 1] == "-":
            b.append(count)
            count = 0
if b == [] or flag == 0:
    print(-1)
    exit()
print(max(b))
