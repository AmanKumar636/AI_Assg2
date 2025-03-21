import csv
import numpy as np
import matplotlib.pyplot as plt

def load_results(csv_file="data/results.csv"):
    algorithms = []
    times = []
    with open(csv_file, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            algorithms.append(row["algorithm"])
            times.append(float(row["time"]))
    return algorithms, times

def compute_average_times(algorithms, times):
    # Convert lists to numpy arrays for easier processing
    algorithms = np.array(algorithms)
    times = np.array(times)
    unique_algos = np.unique(algorithms)
    avg_times = {}
    for algo in unique_algos:
        avg_times[algo] = np.mean(times[algorithms == algo])
    return avg_times

def plot_bar_graph(avg_times):
    # Prepare data for plotting
    algo_names = list(avg_times.keys())
    algo_avg_times = [avg_times[algo] for algo in algo_names]
    
    plt.figure(figsize=(8, 6))
    bars = plt.bar(algo_names, algo_avg_times, color=["blue", "green", "red", "purple"])
    plt.xlabel("Algorithm")
    plt.ylabel("Average Execution Time (s)")
    plt.title("Average Execution Time by Algorithm")
    
    # Annotate bars with their average times
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.0001, f"{yval:.6f}", ha="center", va="bottom")
    
    plt.tight_layout()
    plt.show()

def main():
    algorithms, times = load_results("data/results.csv")
    avg_times = compute_average_times(algorithms, times)
    plot_bar_graph(avg_times)

if __name__ == "__main__":
    main()
