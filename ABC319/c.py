def min_window_width(N, M, L):
    left = 1
    right = sum(L) + M - 1

    while left < right:
        mid = (left + right) // 2
        lines_needed = 1
        line_width = 0

        for word_width in L:
            if line_width + word_width <= mid:
                line_width += word_width + 1
            else:
                lines_needed += 1
                line_width = word_width + 1

        if lines_needed > M:
            left = mid + 1
        else:
            right = mid

    return left

N,M = map(int,input().split())
L = list(map(int, input().split()))
print(min_window_width(N, M, L)) 
