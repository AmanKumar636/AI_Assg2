import math, random

def total_distance(tour, distance_matrix):
    """Calculate total distance of a TSP tour (returns to start)."""
    dist = 0
    n = len(tour)
    for i in range(n):
        dist += distance_matrix[tour[i]][tour[(i + 1) % n]]
    return dist

def generate_distance_matrix(cities):
    """Generate a matrix of Euclidean distances between cities."""
    n = len(cities)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = math.hypot(cities[i][0] - cities[j][0],
                                          cities[i][1] - cities[j][1])
    return matrix

def generate_cities(n, width=100, height=100):
    """Generate a list of n random cities as (x, y) coordinates."""
    return [(random.uniform(0, width), random.uniform(0, height)) for _ in range(n)]

def generate_initial_solution(n):
    """Return a random permutation of city indices as the initial tour."""
    tour = list(range(n))
    random.shuffle(tour)
    return tour

def generate_neighbors(tour):
    """Generate neighbor tours by swapping two cities."""
    neighbors = []
    n = len(tour)
    for i in range(n):
        for j in range(i + 1, n):
            new_tour = tour.copy()
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            neighbors.append(new_tour)
    return neighbors
