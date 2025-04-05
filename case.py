import heapq

# Define the graph (adjacency list with (neighbor, travel_time, cost))
graph = {
    "Chennai": [("Dubai", 4, 500), ("Mumbai", 3.5, 450), ("Doha", 5, 600)],
    "Dubai": [("London", 8, 700)],
    "Mumbai": [("Frankfurt", 7.5, 650)],
    "Doha": [("Paris", 2.5, 680)],
    "London": [("Boston", 7, 400)],
    "Frankfurt": [("Toronto", 6, 500)],
    "Paris": [("Toronto", 6, 450)],
    "Boston": [("New York", 2, 200)],
    "Toronto": [("New York", 3, 300)]
}

# Heuristic values (estimated cost from each city to New York)
heuristic = {
    "Chennai": 1000, "Dubai": 700, "Mumbai": 650, "Doha": 680,
    "London": 400, "Frankfurt": 500, "Paris": 450, "Boston": 200,
    "Toronto": 300, "New York": 0
}

# A* Search Algorithm
def a_star_search(start, goal):
    pq = []  # Priority queue
    heapq.heappush(pq, (0 + heuristic[start], 0, start, []))  # (f, g, city, path)

    while pq:
        f, g, city, path = heapq.heappop(pq)

        if city == goal:
            return path + [city], g  # Return the optimal path and cost

        for neighbor, travel_time, cost in graph.get(city, []):
            new_g = g + cost  # Actual cost to reach the neighbor
            new_f = new_g + heuristic[neighbor]  # f(n) = g(n) + h(n)
            heapq.heappush(pq, (new_f, new_g, neighbor, path + [city]))

    return None, float('inf')  # No path found

# Find the optimal path
optimal_path, total_cost = a_star_search("Chennai", "New York")

# Output the results
print("Optimal Path:", " → ".join(optimal_path))
print("Total Cost: $", total_cost)

import random
def f(x):
    return -x**2 + 4*x
def hill_climbing(function, start, end, step_size=0.1, max_iterations=1000):
    current_x = random.uniform(start, end)
    current_value = function(current_x)
    for _ in range(5):
        next_x = current_x + random.uniform(-step_size, step_size)
        if next_x < start or next_x > end:
            continue       
        next_value = function(next_x)       
        if next_value > current_value:
            current_x = next_x
            current_value = next_value
    for _ in range(max_iterations):
        next_x = current_x + random.uniform(-step_size, step_size)
        if next_x < start or next_x > end:
            continue       
        next_value = function(next_x)
        
        if next_value > current_value:
            current_x = next_x
            current_value = next_value
    return current_x, current_value
start_range = -10
end_range = 10
best_x, best_value = hill_climbing(f, start_range, end_range)
print(f"Best x: {best_x}, Best value: {best_value}")
  