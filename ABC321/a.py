def checker(n):
    digits = str(n)
    for i in range(len(digits) - 1):
        if digits[i] <= digits[i + 1]:
            return False
    return True
N=int(input())
result = checker(N)
print(result)
