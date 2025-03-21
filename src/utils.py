import time
import csv
import os
from search_algorithms import branch_and_bound, ida_star
from optimization_algorithms import hill_climbing_tsp, simulated_annealing_tsp
from environment import FrozenLake

def run_search_experiments(trials=5):
    results = []
    env = FrozenLake()
    print("=== Running Search Algorithms on Frozen Lake ===")
    for i in range(trials):
        sol, cost, iterations, runtime = branch_and_bound(env)
        results.append({
            "algorithm": "BnB",
            "trial": i+1,
            "reward": cost,
            "iterations": iterations,
            "time": runtime
        })
        print(f"BnB Run {i+1}: Reward (cost) = {cost}, Convergence (iterations) = {iterations}, Time = {runtime:.4f}s")
    for i in range(trials):
        sol, threshold, iterations, runtime = ida_star(env)
        results.append({
            "algorithm": "IDA*",
            "trial": i+1,
            "reward": threshold,
            "iterations": iterations,
            "time": runtime
        })
        print(f"IDA* Run {i+1}: Reward (cost) = {threshold}, Convergence (iterations) = {iterations}, Time = {runtime:.4f}s")
    return results

def run_tsp_experiments(trials=5):
    results = []
    print("=== Running TSP Optimization Algorithms ===")
    for i in range(trials):
        sol, cost, iterations, runtime, _ = hill_climbing_tsp()
        results.append({
            "algorithm": "Hill Climbing",
            "trial": i+1,
            "reward": cost,
            "iterations": iterations,
            "time": runtime
        })
        print(f"Hill Climbing Run {i+1}: Reward (tour length) = {cost:.2f}, Convergence (iterations) = {iterations}, Time = {runtime:.4f}s")
    for i in range(trials):
        sol, cost, iterations, runtime, _ = simulated_annealing_tsp()
        results.append({
            "algorithm": "Simulated Annealing",
            "trial": i+1,
            "reward": cost,
            "iterations": iterations,
            "time": runtime
        })
        print(f"Simulated Annealing Run {i+1}: Reward (tour length) = {cost:.2f}, Convergence (iterations) = {iterations}, Time = {runtime:.4f}s")
    return results

def save_results_to_csv(results, filename="data/results.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["algorithm", "trial", "reward", "iterations", "time"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
    print(f"Results saved to {filename}")

def main():
    search_results = run_search_experiments(trials=5)
    tsp_results = run_tsp_experiments(trials=5)
    all_results = search_results + tsp_results
    save_results_to_csv(all_results)

if __name__ == "__main__":
    main()
