import matplotlib
# Use a backend that supports interactive mode (e.g., TkAgg)
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from tsp_helpers import total_distance, generate_cities, generate_distance_matrix

def visualize_tsp_iterative():
    # Parameters
    num_cities = 20
    iterations = 20  # Number of improvement iterations
    pause_time = 1   # Pause time (in seconds) between iterations

    # Generate a fixed set of cities and the corresponding distance matrix
    cities = generate_cities(num_cities)
    distance_matrix = generate_distance_matrix(cities)
    
    # Generate an initial random tour
    tour = list(range(num_cities))
    np.random.shuffle(tour)
    best_tour = tour.copy()
    best_distance = total_distance(best_tour, distance_matrix)
    
    # Set up interactive plotting
    plt.ion()
    fig, ax = plt.subplots()
    
    for i in range(iterations):
        # Create a neighbor solution by swapping two random cities
        new_tour = best_tour.copy()
        idx1, idx2 = np.random.choice(num_cities, size=2, replace=False)
        new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
        new_distance = total_distance(new_tour, distance_matrix)
        
        # Accept the new tour if it's better
        if new_distance < best_distance:
            best_tour = new_tour.copy()
            best_distance = new_distance
        
        # Plot the current tour (cities remain fixed)
        ax.clear()
        cities_np = np.array(cities)
        ax.scatter(cities_np[:, 0], cities_np[:, 1], color='blue', zorder=2)
        
        # Complete the tour by adding the starting city at the end
        cycle = best_tour + [best_tour[0]]
        tour_coords = np.array([cities[j] for j in cycle])
        ax.plot(tour_coords[:, 0], tour_coords[:, 1], color='red', marker='o', zorder=1)
        
        ax.set_title(f"Iteration {i+1}/{iterations}\nTour Length: {best_distance:.2f}")
        ax.set_aspect('equal')
        plt.tight_layout()
        plt.pause(pause_time)  # Display current iteration for 'pause_time' seconds
    
    plt.ioff()  # Turn off interactive mode
    plt.show()

if __name__ == "__main__":
    visualize_tsp_iterative()
