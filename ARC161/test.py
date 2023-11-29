def count_ones(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def find_max_f(N):
    largest_number = -1
    for bit in range(31, -1, -1):
        candidate = largest_number | (1 << bit)
        if count_ones(candidate) == 3 and candidate <= N:
            largest_number = candidate
    return largest_number

T = int(input())
for _ in range(T):
    N = int(input())
    print(find_max_f(N))
