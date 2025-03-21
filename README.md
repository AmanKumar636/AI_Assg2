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
├── README.md                   # Project overview, instructions, and documentation
├── requirements.txt            # List of Python dependencies (e.g., numpy, matplotlib, imageio)
├── src/                        # All source code files
│   ├── environment.py          # Defines the Frozen Lake environment and helper methods
│   ├── search_algorithms.py    # Implements Branch and Bound (BnB) and IDA* for Frozen Lake
│   ├── tsp_helpers.py          # Helper functions for TSP (distance calculations, neighbor generation)
│   ├── optimization_algorithms.py  # Implements Hill Climbing and Simulated Annealing for TSP
│   ├── utils.py                # Runs experiments, records performance (reward, iterations, time), and saves results to CSV
│   ├── visualize_frozen_lake.py  # Generates visualization frames for the Frozen Lake environment
│   └── visualize_tsp.py           # Generates visualization frames for the TSP environment
├── gifs/                       # Contains animated GIFs demonstrating algorithm execution
│   ├── FrozenLake.gif          # Final GIF for the Frozen Lake environment (search algorithms)
│   └── TSP.gif                 # Final GIF for the TSP environment (optimization algorithms)
├── slides/                     # Contains presentation materials
│   └── slide_deck.pdf          # Final presentation slide deck (PDF format)
└── data/                       # Contains experimental output data
    └── results.csv             # CSV file with performance metrics (reward, iterations, time)




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