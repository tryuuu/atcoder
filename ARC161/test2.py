def count_ones(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def find_max_f(n):
    count = 0
    result = 0
    while n:
        count += n & 1
        n >>= 1
        if count == 3:
            return result
        result += 1
    return -1

print(find_max_f(161))
