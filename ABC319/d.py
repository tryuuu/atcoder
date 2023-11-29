from itertools import permutations
from fractions import Fraction

# Testing the function with a sample input
grid = [
    [7, 7, 6],
    [8, 6, 8],
    [7, 7, 6]
]

# This function checks if a given sequence is disappointing
def is_disappointing(sequence):
    for i in range(3):
        if sequence[i][0] == sequence[i][1] and sequence[i][1] != sequence[i][2]:
            return True
        if sequence[0][i] == sequence[1][i] and sequence[1][i] != sequence[2][i]:
            return True

    if sequence[0][0] == sequence[1][1] and sequence[1][1] != sequence[2][2]:
        return True
    
    if sequence[2][0] == sequence[1][1] and sequence[1][1] != sequence[0][2]:
        return True

    return False

# Flatten the grid into a single list
flat_grid = [item for sublist in grid for item in sublist]

# Count the number of valid sequences
valid_count = 0
total_count = 0

# Iterate over all permutations of the numbers in the grid
for perm in permutations(flat_grid):
    # Convert the permutation back into a 3x3 grid
    sequence = [
        [perm[0], perm[1], perm[2]],
        [perm[3], perm[4], perm[5]],
        [perm[6], perm[7], perm[8]]
    ]
    
    total_count += 1
    if not is_disappointing(sequence):
        valid_count += 1

# Calculate the probability
probability = Fraction(valid_count, total_count)

# Convert the probability to a decimal
probability_decimal = valid_count / total_count
print(probability_decimal)





