#!/usr/bin/python
# -*- coding: UTF-8 -*-


import numpy as np
from grid_world import standard_grid, Grid
from utils import *

# Our threshold for terminate
THETA = 1e-3

# Discount the reward to be not greedy or greedy
GAMMA = 0.9

# All possible actions
ALL_POSSIBLE_ACTIONS = ('U', 'D', 'L', 'R')


def init_values() -> dict:
    """ Initiates the all possible values with zero
    
    Return:
        V: All possible values as zeros | dict
    """
    V = {}
    for state in grid.all_states():
        V[state] = 0
    return V

def find_best_action_value_pair(grid: Grid, V: dict, current_state: tuple) -> (str, float):
    """ Tries to find the best action value pair

    Args
        grid: The current instance of the Grid World (game) | Grid
        V: Dict of values for each state | dict
        current_state: Current state, which we want to get the transitions | tuple

    Returns
        action: The best action of this state | str
        float: The best value of this state | float
    """
    # Initiate the best action and value
    best_action = None
    best_value = float('-inf')

    # Set the game to the current state
    grid.set_state(current_state)

    for action in ALL_POSSIBLE_ACTIONS:
        # Get all transtitions s to s' with a
        # [(probability, reward, s'), ...]
        transititions = grid.get_transition_probs(action)
        
        # Initiate the expected value and reward
        expected_reward = 0
        expected_value = 0
        for (probability, reward, state_prime) in transititions:
            # Step 5
            # Sum of all possible rewards * probabilities
            expected_reward += probability * reward
            # Step 6
            # Expected value of s' discounted by their probability
            expected_value += probability * V[state_prime]
        
        # Step 7
        # Heart of value iteration
        current_action_value = expected_reward + GAMMA * expected_value

        # Select the best value at the end and take it
        if current_action_value > best_value:
            best_value = current_action_value
            best_action = action
    return best_action, best_value


def value_iteration(grid: Grid) -> dict:
    """ Performs the value iteration algorithm

    Args
        grid: The current instance of the Grid World (game) | Grid

    Return
        V: Values of every state | dict
    """
    V = init_values()
    
    # Iterate while our threshold is lower then the max change
    while True:
        max_change = 0
        # Loop over all possible states that aren't terminals
        for state in grid.non_terminal_states():
            # Get the old value
            old_value = V[state]

            # Find the new value
            _, new_value = find_best_action_value_pair(grid, V, state)

            # Assign the new value to our table
            V[state] = new_value

            # Calculates the new max_change of our value
            max_change = max(max_change, np.abs(old_value - new_value))
        if max_change < THETA:
            break
    return V

def initialize_random_policy() -> dict:
    """ Inits a random policy with our possivle states

    Return
        policy: A random policy | dict
    """
    # policy is a lookup table for state -> action
    # we'll randomly choose an action and update as we learn
    policy = {}
    for s in grid.non_terminal_states():
        policy[s] = np.random.choice(ALL_POSSIBLE_ACTIONS)
    return policy

def calculate_greedy_policy(grid, V) -> dict:
    """ Calculates the greedy policy of V

    Args
        grid: The current instance of the Grid World (game) | Grid
        V: Values of every state | dict
    
    Return
        policy: The policy is calculated by V | dict
    """
    policy = initialize_random_policy()
    # find a policy that leads to optimal value function
    for state in policy.keys():
        grid.set_state(state)
        # loop through all possible actions to find the best current action
        best_action, _ = find_best_action_value_pair(grid, V, state)
        policy[state] = best_action
    return policy

if __name__ == '__main__':
    # Inits game
    grid = standard_grid(obey_prob=1.0, step_cost=None)
    V = value_iteration(grid)

    # Calculates the optimum policy based on our values
    policy = calculate_greedy_policy(grid, V)

    print("values:")
    print_values(V, grid)
    print("policy:")
    print_policy(policy, grid)