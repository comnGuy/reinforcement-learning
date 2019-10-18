

import numpy as np
from grid_world import standard_grid

theta = 1e-3

def init_values() -> dict:
    values = {}
    for state in grid.all_states():
        values[state] = 0
    return values

def value_iteration(grid):
    values = init_values()
    
    max_change = 1
    while not max_change < theta:
        # 1. Get non terminal states
        # 



if __name__ == '__main__':
  # Init game
  grid = standard_grid(obey_prob=0.5, step_cost=-0.5)
  value_iteration(grid)