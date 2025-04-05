import heapq
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def a_star(start, goal, neighbors_func):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    closed_list = set()
    while open_list:
        current = heapq.heappop(open_list)[1]
        if current in closed_list:
            continue
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal]
        closed_list.add(current)
        for neighbor in neighbors_func(current):
            if neighbor in closed_list:
                continue
            tentative_g_score = g_score[current] + 1  
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    return None, float('inf')
def neighbors(node):
    x, y = node
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
start = (0, 0)
goal = (5, 5)
path, cost = a_star(start, goal, neighbors)
print("Path:", path)
print("Total cost:", cost)