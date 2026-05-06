import itertools

def calculate_total_distance(permutation, distance_matrix):
    total_distance = 0
    for i in range(len(permutation) - 1):
        total_distance += distance_matrix[permutation[i]][permutation[i + 1]]
    total_distance += distance_matrix[permutation[-1]][permutation[0]]  # Return to the starting point
    return total_distance

def traveling_salesman_problem(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    min_distance = float('inf')
    best_permutation = None

    for permutation in itertools.permutations(cities):
        current_distance = calculate_total_distance(permutation, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_permutation = permutation

    return best_permutation, min_distance

# Example usage
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_route, min_distance = traveling_salesman_problem(distance_matrix)
print(f"Best route: {best_route}")
print(f"Minimum distance: {min_distance}")