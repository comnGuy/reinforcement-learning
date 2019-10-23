# Reinforcement Learning

Note: This repository is still in progress to teach me Dynamic Programming and share my results.

**Contents**

1. [Cheat Sheet](#cheat_sheet)
2. [Dynamic Programming](#dynamic_programming)

   2.1 [Value Iteration](#value_iteration)

## <a name="cheat_sheet"></a>Cheat Sheet

![Reinforcement Learning Cheat Sheet](media/reinforcement_learning-overview.png "Reinforcement Learning Cheat Sheet")

## <a name="dynamic_programming"></a>Dynamic Programming

### <a name="value_iteration"></a>Value Iteration

1. Init table V of value estimates with zero
   2. Loop over all possible states
      3. State s loop over all possible actions
         4. Get `a` list of all `s'` transition tuples from `s` and `a`
         5. expected_reward = sum of all possible rewards multiplied by their probabilities
         6. expected_value = lookup `V[s']` for each possible `s'`, mulitply by probabilitiy, sum
         7. actionValue = expectedReward + GAMMA + expectedValue
      4. Set `V[s]` to the best action_value found
   3. Repeat 2-8 until largest change is below threshold

Value Iteration:
[Example Code](https://github.com/comnGuy/reinforcement-learning/tree/master/dynamic_programming/value_iteration)
