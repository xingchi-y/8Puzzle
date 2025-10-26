
goal_state = ['1', '2', '3', '4', '5', '6', '7', '8', 'b']

# check the 8 puzzle can be solved
def is_solvable(state):
    num_of_inversions = 0

    values = [x for x in state if x != 'b']
    for i in range(1, len(values)):
        if values[i] < values[i-1]:
            num_of_inversions += 1

    return num_of_inversions % 2 == 0

# generate all neighboring states by moving the blank tile
def get_neighbors(state):
    neighbors = []
    i = state.index('b')
    moves = []
    if i not in [0, 1, 2]:
        moves.append(-3)  # up
    if i not in [6, 7, 8]:
        moves.append(3)   # down
    if i not in [0, 3, 6]:
        moves.append(-1)  # left
    if i not in [2, 5, 8]:
        moves.append(1)   # right

    for move in moves:
        new_state = state.copy()
        new_state[i], new_state[i + move] = new_state[i + move], new_state[i]
        neighbors.append(new_state)
    return neighbors

# format path for printing
def format_path(path):
    return " → ".join(["(" + " ".join(s) + ")" for s in path])