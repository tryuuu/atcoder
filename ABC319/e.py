from math import ceil

def earliest_time_to_reach(N, X, Y, bus_stops, queries):
    # Step 1: Initialize the time_to_reach array
    time_to_reach = [float('inf')] * N
    time_to_reach[0] = X

    # Step 2: Calculate the time_to_reach array
    for i in range(1, N):
        P, T = bus_stops[i - 1]
        walk_time = time_to_reach[i - 1] + T
        bus_wait_time = ceil(time_to_reach[i - 1] / P) * P
        bus_time = bus_wait_time + T
        time_to_reach[i] = min(walk_time, bus_time)

    # Step 3: Answer the queries
    answers = []
    for query in queries:
        time_to_reach[0] = query + X  # Update the time to reach the first bus stop based on the query time
        # Recalculate the time_to_reach array based on the new starting time
        for i in range(1, N):
            P, T = bus_stops[i - 1]
            walk_time = time_to_reach[i - 1] + T
            bus_wait_time = ceil(time_to_reach[i - 1] / P) * P
            bus_time = bus_wait_time + T
            time_to_reach[i] = min(walk_time, bus_time)
        # Calculate the earliest time to reach Aoki's house and add it to the answers list
        answers.append(time_to_reach[N - 1] + Y)
    
    return answers

# Get the values of N, X and Y
N, X, Y = map(int, input().split())

# Get the values of P and T for each bus stop
bus_stops = [tuple(map(int, input().split())) for _ in range(N - 1)]

# Get the number of queries and the query values
Q = int(input())
queries = [int(input()) for _ in range(Q)]

# Now you can call the function with the inputs
answers = earliest_time_to_reach(N, X, Y, bus_stops, queries)

# Print the answers
for answer in answers:
    print(answer)
