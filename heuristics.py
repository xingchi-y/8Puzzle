
from utils import goal_state

# number of misplaced tiles
def h_num_of_misplaced(state):
    num = 0
    for i in range(9):
        if state[i] != 'b' and state[i] != goal_state[i]:
            num += 1

    return num

# total Manhattan distance
def h_manhattan_distance(state):
    dist = 0
    for i, val in enumerate(state):
        if val != 'b':
            goal_i = goal_state.index(val)
            x1, y1 = i // 3, i % 3
            x2, y2 = goal_i // 3, goal_i % 3
            dist += abs(x1 - x2) + abs(y1 - y2)
    return dist

# total index distance in an array
def h_array_distance(state):
    dist = 0
    for i, val in enumerate(state):
        if val != 'b':
            goal_i = goal_state.index(val)
            dist += abs(i - goal_i)
    return dist