
from queue import PriorityQueue
def best_first_search(graph,start,end,heuristic):
#     initialise a priority queue object
    frontier = PriorityQueue()
#     append the priority queue with the start node
    frontier.put(start,heuristic[start])
#     dictionary to store the parent of each node
    came_from = {}
#     as start is the root node it dosent have a parent
    came_from[start] = None
#     loop until all nodes in the priority queue are removed
    while not frontier.empty():
        current  = frontier.get()
        if current == goal:
            path=[]
            while current is not None:
                path.append(current)
                current =  came_from[current]
            return path[::-1]
        for next_node in graph[current]:
            if next_node  not in came_from:
                priority = heuristic[next_node]
                frontier.put(next_node,priority)
                came_from[next_node] =current
    return None #returning none if the goal is not reachable


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'
path = best_first_search(graph,start,goal,heuristic)
print("Path from", start, "to", goal, ":", path)