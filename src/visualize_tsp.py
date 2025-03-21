# src/visualize_tsp.py
import matplotlib.pyplot as plt
import numpy as np
import random
import time

def generate_cities(n, width=100, height=100):
    return [(random.uniform(0, width), random.uniform(0, height)) for _ in range(n)]

def total_distance(tour, cities):
    dist = 0
    n = len(tour)
    for i in range(n):
        city_a = cities[tour[i]]
        city_b = cities[tour[(i+1) % n]]
        dist += np.hypot(city_a[0] - city_b[0], city_a[1] - city_b[1])
    return dist

def plot_tour(cities, tour, iteration, total_dist):
    plt.clf()
    cities = np.array(cities)
    # Plot cities
    plt.scatter(cities[:, 0], cities[:, 1], color='blue')
    # Plot tour: connect cities in order
    tour_cities = cities[tour + [tour[0]]]  # add start city at end to complete loop
    plt.plot(tour_cities[:, 0], tour_cities[:, 1], color='red', linestyle='-', marker='o')
    plt.title(f"Iteration: {iteration} | Total Distance: {total_dist:.2f}")
    plt.pause(0.5)

def simulate_tsp():
    num_cities = 20
    cities = generate_cities(num_cities)
    # Start with a random tour
    tour = list(range(num_cities))
    random.shuffle(tour)
    
    plt.ion()
    fig = plt.figure()
    
    # Simulate improvement using a simple "swap" heuristic
    best_distance = total_distance(tour, cities)
    iterations = 0
    max_iterations = 20  # adjust number of iterations for demonstration
    
    while iterations < max_iterations:
        iterations += 1
        # Create a neighbor by swapping two random cities
        new_tour = tour.copy()
        i, j = random.sample(range(num_cities), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        new_distance = total_distance(new_tour, cities)
        
        # Accept the new tour if it's better (for demonstration)
        if new_distance < best_distance:
            tour = new_tour
            best_distance = new_distance
        
        plot_tour(cities, tour, iterations, best_distance)
    
    plt.ioff()
    plt.show()
    
if __name__ == "__main__":
    simulate_tsp()
