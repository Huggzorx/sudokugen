import numpy as np
import pandas as pd
import random

def gen_solved_puzzle() -> np.ndarray:
    # Create blank grid
    puzzle = np.zeros(shape=(9, 9), dtype=int)

    # Dataframe to hold values that have been tried for each cell
    tried_nums = pd.DataFrame([[[] for i in range(9)] for i in range(9)])

    step_count = 0
    cell_num = 0
    while cell_num < 81:
        row_num = cell_num//9
        col_num = cell_num%9

        # Get all valid values for this cell, except for ones we used before
        valid_vals = list(set(valid_cell_values(puzzle, row_num, col_num)).difference(set(tried_nums.iloc[row_num, col_num])))
        if len(valid_vals) > 0:
            # Pick a random valid value and add it to the list of used values for this cell
            rand_val = random.choice(valid_vals)
            puzzle[row_num, col_num] = rand_val
            tried_nums.iloc[row_num, col_num].append(rand_val)
            cell_num += 1
        else:
            # No valid vals, so clear the cell and its history, and go back one cell
            puzzle[row_num, col_num] = 0
            tried_nums.iloc[row_num, col_num] = []
            cell_num -= 1

        step_count += 1

    print('\nCompleted in', step_count, 'steps!')
    print_puzzle(puzzle)

    return puzzle

def valid_cell_values(puzzle: np.ndarray, row_num: int, col_num: int) -> list:
    box_row = row_num//3
    box_col = col_num//3

    nums_in_box = set(puzzle[box_row*3:(box_row*3)+3, box_col*3:(box_col*3)+3].flatten())
    nums_in_row = set(puzzle[row_num, :])
    nums_in_col = set(puzzle[:, col_num])

    invalid_nums = nums_in_row.union(nums_in_col).union(nums_in_box)
    valid_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}.difference(invalid_nums)

    return list(valid_nums)

def print_puzzle(puzzle: np.ndarray) -> None:

    puzzle_str = puzzle.astype(str)

    print()
    for row_num in range(9):
        if row_num % 3 == 0:
            print('-'*25)
        
        row = puzzle_str[row_num]
        print('| ' + ' '.join(row[0:3]) + ' | ' + ' '.join(row[3:6]) + ' | ' + ' '.join(row[6:]) + ' |')

    print('-'*25)

    return None