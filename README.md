# AI Assignment 2: Search and Optimization

This project implements and evaluates search and optimization algorithms on two distinct environments:

- **Search Algorithms (on Frozen Lake Environment)**
  - **Branch and Bound (BnB)**
  - **Iterative Deepening A\*** (IDA*)

- **Optimization Algorithms (for the Travelling Salesman Problem, TSP)**
  - **Hill Climbing (HC)**
  - **Simulated Annealing (SA)**

The goal is to compare their performance in terms of reward/cost, time, and convergence characteristics.

## Repository Structure

AI_Assg2/
├── README.md                  # Overview and instructions
├── requirements.txt           # List of dependencies
├── src/                       # All source code
│   ├── environment.py         # Frozen Lake environment definition
│   ├── search_algorithms.py   # BnB and IDA* implementations
│   ├── tsp_helpers.py         # Helper functions for TSP
│   ├── optimization_algorithms.py  # Hill Climbing and SA for TSP
│   ├── utils.py               # Script to run experiments & record performance
│   └── plot_results.py        # Script to generate bar charts from results
├── slides/                    # Presentation slide deck(s)
│   └── slide_deck.pdf         # Your slide deck file (PDF format)
├── gifs/                      # Animated GIFs of algorithm execution
│   ├── FrozenLake.gif         # GIF showing the Frozen Lake algorithm in action
│   └── TSP.gif                # GIF showing the TSP algorithm execution
├── bar_charts/                # Generated bar charts (or saved images)
│   └── execution_time_bar_chart.png  # Bar chart image file (or other formats)
└── data/                      # Experimental data output
    └── results.csv            # CSV file with performance metrics




## Dependencies

This project requires Python 3.x along with the following libraries:

- `numpy`
- `matplotlib`

Install these dependencies by running:

```bash
pip install -r requirements.txt


Running the Experiments
To execute the experiments and generate the results:

python src/utils.py

This script will:

Run the search algorithms (BnB and IDA*) on the Frozen Lake environment.
Run the optimization algorithms (Hill Climbing and Simulated Annealing) on a TSP instance.
Print out metrics (cost, iterations, runtime) for each run (5 trials per algorithm).
Save the results to data/results.csv.
Display a bar chart comparing the average execution times.