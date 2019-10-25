# Reinforcement Learning

Note: This repository is still in progress to teach me Dynamic Programming and share my results.

**Contents**

1. [Cheat Sheet](#cheat_sheet)
2. [Dynamic Programming](#dynamic_programming)

   2.1 [Value Iteration](#value_iteration)

   2.2 [Policy Iteration](#policy_iteration)

3. [References](#references)

## <a name="cheat_sheet"></a>Cheat Sheet

![Reinforcement Learning Cheat Sheet](media/reinforcement_learning-overview.png "Reinforcement Learning Cheat Sheet")

## <a name="dynamic_programming"></a>Dynamic Programming

### <a name="value_iteration"></a>Value Iteration

**Formula**

<img src="https://latex.codecogs.com/gif.latex?V_{i&plus;1}(s)&space;:=&space;\max*a&space;\left\{&space;\sum\*{s'}&space;P_a(s,s')&space;\left(&space;R_a(s,s')&space;&plus;&space;\gamma&space;V_i(s')&space;\right)&space;\right\}" title="\Large x=V_{i+1}(s) := \max_a \left\{ \sum\*{s'} P_a(s,s') \left( R_a(s,s') + \gamma V_i(s') \right) \right\}" />

**Algorithm**

1. Init table V of value estimates with zero
   1. Loop over all possible states
      1. State s loop over all possible actions
         1. Get `a` list of all `s'` transition tuples from `s` and `a`
         2. expected_reward = sum of all possible rewards multiplied by their probabilities
         3. expected_value = lookup `V[s']` for each possible `s'`, mulitply by probabilitiy, sum
         4. `actionValue = expectedReward + GAMMA + expectedValue`
      2. Set `V[s]` to the best action_value found
   2. Repeat _i_ until largest change is below threshold

Value Iteration:
[Example Code](https://github.com/comnGuy/reinforcement-learning/tree/master/dynamic_programming/value_iteration)

### <a name="policy_iteration"></a>Policy Iteration

**Formula**

**Algorithm**

## <a name="references"></a>References

- Kallenberg 2002
- Movie 37
