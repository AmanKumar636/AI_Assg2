import time, math, random
from tsp_helpers import total_distance, generate_cities, generate_distance_matrix, generate_initial_solution, generate_neighbors

def hill_climbing_tsp(num_cities=20):
    start_time = time.time()
    cities = generate_cities(num_cities)
    distance_matrix = generate_distance_matrix(cities)
    current_solution = generate_initial_solution(num_cities)
    current_cost = total_distance(current_solution, distance_matrix)
    iterations = 0

    while True:
        iterations += 1
        neighbors = generate_neighbors(current_solution)
        best_neighbor = None
        best_neighbor_cost = float('inf')
        for neighbor in neighbors:
            cost = total_distance(neighbor, distance_matrix)
            if cost < best_neighbor_cost:
                best_neighbor_cost = cost
                best_neighbor = neighbor
        if best_neighbor_cost < current_cost:
            current_solution = best_neighbor
            current_cost = best_neighbor_cost
        else:
            break  # local optimum reached
        if time.time() - start_time > 600:
            print("Timeout reached in Hill Climbing TSP.")
            break

    runtime = time.time() - start_time
    return current_solution, current_cost, iterations, runtime, cities

def simulated_annealing_tsp(num_cities=20, initial_temp=1000, cooling_rate=0.995):
    start_time = time.time()
    cities = generate_cities(num_cities)
    distance_matrix = generate_distance_matrix(cities)
    current_solution = generate_initial_solution(num_cities)
    current_cost = total_distance(current_solution, distance_matrix)
    temp = initial_temp
    iterations = 0

    while temp > 1e-3:
        iterations += 1
        i, j = random.sample(range(num_cities), 2)
        neighbor = current_solution.copy()
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        neighbor_cost = total_distance(neighbor, distance_matrix)
        delta = neighbor_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_solution = neighbor
            current_cost = neighbor_cost
        temp *= cooling_rate
        if time.time() - start_time > 600:
            print("Timeout reached in Simulated Annealing TSP.")
            break

    runtime = time.time() - start_time
    return current_solution, current_cost, iterations, runtime, cities
