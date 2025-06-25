"""Simplified Counterfactual Regret Minimization implementation."""
from __future__ import annotations

import random
from collections import defaultdict
from typing import Dict, Tuple

Action = str


class CFRNode:
    def __init__(self, actions: Tuple[Action, ...]):
        self.actions = actions
        self.regret_sum = defaultdict(float)
        self.strategy_sum = defaultdict(float)

    def get_strategy(self) -> Dict[Action, float]:
        positive_regrets = [max(0.0, self.regret_sum[a]) for a in self.actions]
        normalizing_sum = sum(positive_regrets)
        if normalizing_sum > 0:
            strategy = {a: r / normalizing_sum for a, r in zip(self.actions, positive_regrets)}
        else:
            uniform_prob = 1.0 / len(self.actions)
            strategy = {a: uniform_prob for a in self.actions}
        for a, p in strategy.items():
            self.strategy_sum[a] += p
        return strategy

    def get_average_strategy(self) -> Dict[Action, float]:
        normalizing_sum = sum(self.strategy_sum.values())
        if normalizing_sum == 0:
            return {a: 1.0 / len(self.actions) for a in self.actions}
        return {a: self.strategy_sum[a] / normalizing_sum for a in self.actions}


class CFRTrainer:
    def __init__(self):
        self.node = CFRNode(actions=("fold", "call", "raise"))

    def train(self, iterations: int = 1000):
        for _ in range(iterations):
            self.cfr()

    def cfr(self):
        strategy = self.node.get_strategy()
        # Placeholder: compute utilities of actions and update regrets
        # In a real system, this would traverse the game tree.
        util = random.random()
        for a in self.node.actions:
            regret = util - random.random()
            self.node.regret_sum[a] += regret

    def get_action(self) -> Action:
        strategy = self.node.get_average_strategy()
        actions, probs = zip(*strategy.items())
        return random.choices(actions, probs)[0]
