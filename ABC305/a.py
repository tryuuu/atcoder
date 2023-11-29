def a(distance):
    stations = [5 * i for i in range(22)]
    y=min(stations,key=lambda x:abs(x-distance))
    return y
N=int(input())
print(a(N))