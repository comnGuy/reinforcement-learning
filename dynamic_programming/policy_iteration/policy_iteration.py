#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import grid_world
import utils
import random


### Game Settings
# Cost per step
STEP_COST = None
# How much random is in the game
OBEY_PROB = 1.0
# All possible actions
ALL_POSSIBLE_ACTIONS = ('U', 'D', 'L', 'R')


### Value Iteration Settings
# Discount the reward to be not greedy or greedy
GAMMA = 1.0
# Max iterations
MAX_ITERATIONS = 5


class PolicyIteration:
    def __init__(self, environment: grid_world.Grid, gamma: float = 1.0, max_iterations: int = 10000):
        self._environment = environment
        self._gamma = gamma
        self._max_iteration = max_iterations

        self.policy = {}

    def run(self):
        """ Runs Value Iteration """
        for iteration in range(self._max_iteration):
            # Compute values

            # Extract policy
            print(iteration)

    def init_random_policy(self):
        """ Inits a random policy with our possivle states """
        for state in self._environment.all_states():
            self.policy[state] = random.randint(0, len(ALL_POSSIBLE_ACTIONS))
    
    def compute_values_policy(self):
        pass


if __name__ == '__main__':
    # Inits game
    environment = grid_world.standard_grid(obey_prob=OBEY_PROB, step_cost=STEP_COST)

    # Inits Policy Iteration class
    policy_iteration = PolicyIteration(environment, gamma=GAMMA, max_iterations=MAX_ITERATIONS)

    policy_iteration.init_random_policy()
    policy_iteration.run()