"""Short-horizon replanning over empirical state transitions."""

from __future__ import annotations

from functools import lru_cache

from .hypotheses import ActionKey
from .memory import CompactMemory
from .state import StructuredState
from .world_model import WorldModel


class ShortHorizonPlanner:
    def __init__(
        self,
        world_model: WorldModel,
        memory: CompactMemory,
        horizon: int = 2,
        confidence_threshold: float = 0.68,
    ) -> None:
        self.world_model = world_model
        self.memory = memory
        self.horizon = horizon
        self.confidence_threshold = confidence_threshold

    def action_values(
        self, state: StructuredState, actions: list[ActionKey]
    ) -> dict[ActionKey, float]:
        @lru_cache(maxsize=128)
        def future_value(fingerprint: str, depth: int) -> float:
            if depth <= 0:
                return self.memory.state_novelty(fingerprint)
            edges = self.world_model.known_edges(fingerprint)
            if not edges:
                return self.memory.state_novelty(fingerprint)
            return max(
                confidence
                * (self.memory.state_novelty(target) + 0.55 * future_value(target, depth - 1))
                for _, target, confidence in edges
            )

        values: dict[ActionKey, float] = {}
        for action in actions:
            prediction = self.world_model.predict(state, action)
            if (
                prediction.next_state is None
                or prediction.confidence < self.confidence_threshold
            ):
                values[action] = 0.0
                continue
            values[action] = prediction.confidence * (
                2.0 * prediction.expected_progress
                + self.memory.state_novelty(prediction.next_state)
                + 0.55 * future_value(prediction.next_state, self.horizon - 1)
            )
        return values
