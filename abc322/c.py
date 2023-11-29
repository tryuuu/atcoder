import bisect
n,m = map(int,input().split())
a = list(map(int, input().split()))

def binary_search(n, a):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == n:
            return a[mid]
        elif a[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    return a[left] if left < len(a) else None

for i in range(1,n+1):
    num = binary_search(i,a)
    print(num-i)




