import heapq
def a_star_search(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]
    came_from = {}
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        for neighbor, cost in graph[current].items():
            temp_g = g_score[current] + cost
            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score[neighbor] = temp_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    return None

graph={'A':{'B':4,'C':3},
       'B':{'A':4,'E':12,'F':5},
       'C':{'A':3,'D':7,'E':10},
       'D':{'C':7,'E':2},
       'E':{'B':12,'C':10,'D':2,'Z':5},
       'F':{'B':5,'Z':16},
       'Z':{'E':5,'F':16}}
heuristic={'A':14,'B':12,'C':11,'D':6,'E':4,'F':11,'Z':0}
start='A'
goal='Z'
path=a_star_search(graph,start,goal,heuristic)
print(path)
print("A* Path and Cost Calculation:")
path = a_star_search(graph, start, goal, heuristic)
print(f"A* Path: {'->'.join(path)}")
cost = sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
print(f"Total Cost: {cost}")



