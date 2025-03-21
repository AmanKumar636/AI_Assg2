# src/utils.py
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
from search_algorithms import branch_and_bound, ida_star
from optimization_algorithms import hill_climbing_tsp, simulated_annealing_tsp
from environment import FrozenLake

def run_search_experiments(trials=5):
    bnb_times = []
    ida_times = []
    env = FrozenLake()
    print("=== Running Search Algorithms on Frozen Lake ===")
    for i in range(trials):
        sol, cost, iterations, runtime = branch_and_bound(env)
        bnb_times.append(runtime)
        print(f"BnB Run {i+1}: Cost = {cost}, Iterations = {iterations}, Time = {runtime:.4f}s")
    for i in range(trials):
        sol, bound, iterations, runtime = ida_star(env)
        ida_times.append(runtime)
        print(f"IDA* Run {i+1}: Bound = {bound}, Iterations = {iterations}, Time = {runtime:.4f}s")
    return bnb_times, ida_times

def run_tsp_experiments(trials=5):
    hc_times = []
    sa_times = []
    print("=== Running TSP Optimization Algorithms ===")
    for i in range(trials):
        sol, cost, iterations, runtime, _ = hill_climbing_tsp()
        hc_times.append(runtime)
        print(f"Hill Climbing Run {i+1}: Cost = {cost:.2f}, Iterations = {iterations}, Time = {runtime:.4f}s")
    for i in range(trials):
        sol, cost, iterations, runtime, _ = simulated_annealing_tsp()
        sa_times.append(runtime)
        print(f"Simulated Annealing Run {i+1}: Cost = {cost:.2f}, Iterations = {iterations}, Time = {runtime:.4f}s")
    return hc_times, sa_times

def save_results_csv(bnb_times, ida_times, hc_times, sa_times):
    with open('data/results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Algorithm", "Trial", "Time (s)"])
        for i, t in enumerate(bnb_times):
            writer.writerow(["BnB", i+1, t])
        for i, t in enumerate(ida_times):
            writer.writerow(["IDA*", i+1, t])
        for i, t in enumerate(hc_times):
            writer.writerow(["Hill Climbing", i+1, t])
        for i, t in enumerate(sa_times):
            writer.writerow(["Simulated Annealing", i+1, t])
    print("Results saved to data/results.csv")

def plot_results(bnb_times, ida_times, hc_times, sa_times):
    algorithms = ['BnB', 'IDA*', 'HC', 'SA']
    avg_times = [np.mean(bnb_times), np.mean(ida_times), np.mean(hc_times), np.mean(sa_times)]
    
    plt.figure(figsize=(8, 6))
    plt.bar(algorithms, avg_times, color=['blue', 'green', 'red', 'purple'])
    plt.xlabel('Algorithm')
    plt.ylabel('Average Time (s)')
    plt.title('Average Time to Reach Goal/Optimum')
    plt.show()

if __name__ == "__main__":
    # Run experiments for search algorithms (Frozen Lake)
    bnb_times, ida_times = run_search_experiments(trials=5)
    # Run experiments for TSP optimization algorithms
    hc_times, sa_times = run_tsp_experiments(trials=5)
    # Save results to CSV
    save_results_csv(bnb_times, ida_times, hc_times, sa_times)
    # Plot the results
    plot_results(bnb_times, ida_times, hc_times, sa_times)
