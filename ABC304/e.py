for i in range(A + 1):
        x = i * W // (A + 1)
        for j in range(B + 1):
            y = j * H // (B + 1)
            count = 0
            for p, q in strawberries:
                if p <= x and q <= y:
                    count += 1
            min_strawberries = min(min_strawberries, count)
            max_strawberries = max(max_strawberries, count)