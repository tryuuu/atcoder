N=int(input())
S=input()
def count_consecutive_gts(s):
    counts = []
    count = 0

    for char in s:
        if char == '>':
            count += 1
        elif count > 0:
            counts.append(count)
            count = 0

    if count > 0:
        counts.append(count)

    return counts

def calculator(n):
    return n*(n+1)//2

def solver():
    answer = 0
    num_list = count_consecutive_gts(S)
    for num in num_list:
        answer += calculator(num)
    print(answer)

solver()





