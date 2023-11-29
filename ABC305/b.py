distances = {
    'A': 0,
    'B': 3,
    'C': 1,
    'D': 4,
    'E': 1,
    'F': 5,
    'G': 9
}

def calculate_distance(p, q):
    if p == q:
        return 0
    elif p < q:
        return sum(distances[point] for point in distances if p < point <= q)
    else:
        return sum(distances[point] for point in distances if q < point <= p)

p,q = input().split()

distance = calculate_distance(p, q)
print(distance)


