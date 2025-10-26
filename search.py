
from utils import *
import heapq

# Greedy Best-First Search
def greedy_best_first(start, heuristic, max_steps = 1000):
    frontier = []
    heapq.heappush(frontier, (heuristic(start), start, []))
    visited = set()
    steps = 0

    while frontier:
        steps += 1
        if steps > max_steps:
            return None

        h, state, path = heapq.heappop(frontier)
        if state == goal_state:
            return path + [state]

        visited.add(tuple(state))
        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in visited:
                heapq.heappush(frontier, (heuristic(neighbor), neighbor, path + [state]))
    return None

# A* Search
def astar(start, heuristic, max_steps = 1000):
    frontier = []
    heapq.heappush(frontier, (heuristic(start), 0, start, []))
    visited = set()
    steps = 0

    while frontier:
        steps += 1
        if steps > max_steps:
            return None

        f, g, state, path = heapq.heappop(frontier)
        if state == goal_state:
            return path + [state]

        visited.add(tuple(state))
        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in visited:
                g_new = g + 1
                f_new = g_new + heuristic(neighbor)
                heapq.heappush(frontier, (f_new, g_new, neighbor, path + [state]))
    return None