
from heuristics import *
from search import *

def main():
    # state = ['1', '2', '3', 'b', '4', '6', '8', '5', '7']
    # state = ['b', '1', '3', '4', '2', '5', '7', '8', '6']
    # if is_solvable(state):
    #     print('Solvable')
    # else:
    #     print('Not solvable')

    start_states = [
        ['b', '1', '3', '4', '2', '5', '7', '8', '6'],
        ['4', '5', 'b', '6', '1', '8', '7', '3', '2'],
        ['1', '3', 'b', '4', '2', '5', '7', '8', '6'],
        ['8', '6', '7', '2', '5', '4', '3', 'b', '1'],
        ['1', '2', '3', 'b', '4', '5', '6', '7', '8']
    ]

    algorithms = [greedy_best_first, astar]
    heuristics = [h_num_of_misplaced, h_manhattan_distance, h_array_distance]

    # run 2 algorithms
    for algo in algorithms:
        print(f"\n{algo.__name__} search:")
        # run 3 heuristics
        for h in heuristics:
            print(f"\n{h.__name__}:")
            run_experiment(algo, h, start_states)
        print("-" * 100)


def run_experiment(algorithm, heuristic_fn, start_states):
    path_lengths = []
    for idx, start_state in enumerate(start_states, 1):
        if not is_solvable(start_state):
            print("Not solvable.")
            continue

        result = algorithm(start_state, heuristic_fn)

        if result:
            path_len = len(result) - 1
            path_lengths.append(path_len)
            print(format_path(result))
        else:
            print(f"No solution found (max steps reached).")

    if path_lengths:
        avg_path = sum(path_lengths) / len(path_lengths)
        print(f"Average number of steps: {avg_path:.2f}")



if __name__ == "__main__":
    main()