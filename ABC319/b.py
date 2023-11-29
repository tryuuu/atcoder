def divide(n):
    divide_list = []
    for i in range(1,10):
        if n%i==0:
            divide_list.append(i)
    return divide_list

def changer(n):
    answer = "1"
    divide_list =  divide(n)
    for i in range(1,n+1):
        for j in divide_list:
            if i%(n//j)==0:
                answer += str(j)
                break
            elif j==divide_list[len(divide_list)-1]:
                answer += "-"
    return answer
N=int(input())
print(changer(N))
