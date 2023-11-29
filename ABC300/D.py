import math

n = int(input())
ans = 0

for a in range(2, int(math.sqrt(n)) + 1):
    for b in range(a, int(n**(1/3)) + 1):
        c = int(n / (a**2 * b)) + 1
        if a**2 * b * c <= n and a < b and b < c and math.gcd(a, b) == math.gcd(b, c) == 1:
            ans += 1

print(ans)

