import heapq
def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = set()
    while priority_queue:
         cost, node, path = heapq.heappop(priority_queue) 
         if node in visited:
              continue
         path = path + [node]
         visited.add(node)
         if node == goal:
              return cost, path
         for neighbor, edge_cost in graph.get(node, []):
              if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path))
float('inf'), []
graph = {
   'A': [('B', 2), ('C', 3)],
   'B': [('A', 2), ('D', 1), ('E', 5)],
   'C': [('A', 3), ('F', 6)],
   'D': [('B', 1)],
   'E': [('B', 5), ('G', 2)],
   'F': [('C', 6)],
   'G': [('E', 2)]
}
start_node = 'A'
goal_node = 'G'
cost, path = uniform_cost_search(graph, start_node, goal_node)
print(f"Least-cost path from {start_node} to {goal_node}: {path}")
print(f"Total Cost: {cost}")
 