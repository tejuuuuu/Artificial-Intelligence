def a_star_search(self, start, goal):
    queue = [(0 + self.heuristic[start], 0, start, [start])]  # (f, g, node, path)
    visited = set()
    while queue:
        f, g, node, path = heapq.heappop(queue)
        if node == goal:
            return path, g  # Return path and its total cost
        if node not in visited:
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    new_g = g + self.weights.get((node, neighbor), 1)
                    new_f = new_g + self.heuristic.get(neighbor, 0)
                    heapq.heappush(queue, (new_f, new_g, neighbor, path + [neighbor]))
    return [], 0  # In case no path is found

Graph.a_star_search = a_star_search
from collections import defaultdict
import heapq

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.weights = {}
        self.heuristic = {}

    def addedges(self, u, v, weight: int = 1):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.weights[(u, v)] = weight
        self.weights[(v, u)] = weight

    def set_heuristics(self, node, value):
        self.heuristic[node] = value

    def print_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {', '.join(neighbors)}")

    def ucs_search(self, start, goal):
        queue = [(0, start, [start])]  
        visited = set()
        while queue:
            cost, node, path = heapq.heappop(queue)
            if node == goal:
                return path, cost  # Return path and its total cost
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        new_cost = cost + self.weights.get((node, neighbor), 1)
                        heapq.heappush(queue, (new_cost, neighbor, path + [neighbor]))
        return [], 0  # In case no path is found

# Create the graph
g = Graph()
edges = [('A', 'B', 4), ('A', 'C', 3),
         ('C', 'E', 10), ('C', 'D', 7),
         ('D', 'E', 2),
         ('B', 'E', 12), ('B', 'F', 5),
         ('F', 'Z', 16),
         ('E', 'Z', 5)]
heuristics = {'A': 14, 'B': 12, 'C': 11, 'E': 4, 'D': 6, 'F': 11, 'Z': 0}
for edge in edges:
    g.addedges(*edge)
for node, value in heuristics.items():
    g.set_heuristics(node, value)
start, goal = 'A', 'Z'
print("The graph:\n")
g.print_graph()
print("\nPath and Cost Calculation:")
path, cost = g.ucs_search(start, goal)
print(f"UCS Path: {'->'.join(path)}")
print(f"Total Cost: {cost}")