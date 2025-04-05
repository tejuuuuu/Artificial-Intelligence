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
    def heuristic_function(self, node, goal):
        return self.heuristic.get(node, 0)
    def astar_search(self, start, goal):
        open_list = []  
        closed_list = set()  
        g_start = 0
        h_start = self.heuristic_function(start, goal)
        heapq.heappush(open_list, (h_start, g_start, start, [start])) 
        while open_list:
            f, g_cost, node, path = heapq.heappop(open_list)  
            if node == goal:
                return path, g_cost 
            if node in closed_list:
                continue            
            closed_list.add(node)  
            for neighbor in self.graph[node]:
                if neighbor not in closed_list:
                    g_new = g_cost + self.weights.get((node, neighbor), 1) 
                    h_new = self.heuristic_function(neighbor, goal)  
                    f_new = g_new + h_new
                    heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))  
        return [], 0  
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
c