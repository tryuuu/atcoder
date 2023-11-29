def checker(num):
    num_str = str(num)
    for i in range(len(num_str) - 1):
        if num_str[i] <= num_str[i+1]:
            return False
    return True

def find_number(K):
    current_num = 1
    count = 0
    
    while True:
        if checker(current_num):
            count += 1
            if count == K:
                return current_num
        current_num += 1

K = int(input())
result = find_number(K)
print(result)

