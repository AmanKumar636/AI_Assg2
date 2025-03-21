# src/search_algorithms.py
import time
from environment import FrozenLake

def branch_and_bound(env: FrozenLake):
    start_time = time.time()
    best_solution = None
    best_cost = float('inf')
    # Each element in the stack is: (current position, cost so far, path taken)
    stack = [(env.start, 0, [env.start])]
    iterations = 0

    while stack:
        iterations += 1
        pos, cost, path = stack.pop()
        if env.is_goal(pos):
            if cost < best_cost:
                best_cost = cost
                best_solution = path
        else:
            for neighbor in env.neighbors(pos):
                # Prevent cycles: only add neighbor if it's not already in the current path.
                if neighbor in path:
                    continue
                step_cost = 1  # constant step cost
                new_cost = cost + step_cost
                # Prune if estimated total cost exceeds current best solution.
                if new_cost + env.heuristic(neighbor) < best_cost:
                    stack.append((neighbor, new_cost, path + [neighbor]))
        # Timeout condition to avoid endless run (10 minutes)
        if time.time() - start_time > 600:
            print("Timeout reached in Branch and Bound.")
            break

    runtime = time.time() - start_time
    return best_solution, best_cost, iterations, runtime

def ida_star(env: FrozenLake):
    start_time = time.time()
    threshold = env.heuristic(env.start)
    path = [env.start]
    iterations = 0

    def search(path, g, threshold):
        nonlocal iterations
        iterations += 1
        node = path[-1]
        f = g + env.heuristic(node)
        if f > threshold:
            return None, f
        if env.is_goal(node):
            return path, f
        min_threshold = float('inf')
        for neighbor in env.neighbors(node):
            if neighbor not in path:  # avoid cycles
                path.append(neighbor)
                result, temp_threshold = search(path, g + 1, threshold)
                if result is not None:
                    return result, temp_threshold
                if temp_threshold < min_threshold:
                    min_threshold = temp_threshold
                path.pop()
        return None, min_threshold

    while True:
        result, new_threshold = search(path, 0, threshold)
        if result is not None:
            runtime = time.time() - start_time
            return result, threshold, iterations, runtime
        if new_threshold == float('inf'):
            runtime = time.time() - start_time
            return None, threshold, iterations, runtime
        threshold = new_threshold
        if time.time() - start_time > 600:
            print("Timeout reached in IDA*.")
            break
