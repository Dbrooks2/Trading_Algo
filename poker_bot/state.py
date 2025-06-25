"""Game state representation for Texas Hold'em."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple, Dict

Card = Tuple[str, str]  # (rank, suit)


@dataclass
class PlayerState:
    position: str
    stack: int
    hole_cards: List[Card] = field(default_factory=list)
    bet: int = 0


@dataclass
class GameState:
    players: Dict[str, PlayerState] = field(default_factory=dict)
    community_cards: List[Card] = field(default_factory=list)
    pot: int = 0
    betting_history: List[str] = field(default_factory=list)

    def update_from_detection(self, detection: Dict[str, List[Card]]):
        """Update game state from vision detection output."""
        for key, cards in detection.items():
            if key == "community":
                self.community_cards = cards
            elif key in self.players:
                self.players[key].hole_cards = cards

    def record_action(self, player: str, action: str):
        """Record a player's action."""
        self.betting_history.append(f"{player}:{action}")
