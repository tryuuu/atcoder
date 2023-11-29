def approximate_number(n):
    if n <= 10**3 - 1:
        return n
    elif n <= 10**4 - 1:
        return n // 10 * 10
    elif n <= 10**5 - 1:
        return n // 100 * 100
    elif n <= 10**6 - 1:
        return n // 1000 * 1000
    elif n <= 10**7 - 1:
        return n // 10000 * 10000
    elif n <= 10**8 - 1:
        return n // 100000 * 100000
    else:
        return n // 1000000 * 1000000

n = int(input())

x = approximate_number(n)
print(x)
