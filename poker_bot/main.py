"""Entry point for the poker bot."""
from __future__ import annotations

import time
from typing import Optional

from vision import grab_frame, detect_cards
from state import GameState, PlayerState
from cfr import CFRTrainer


def setup_game() -> GameState:
    state = GameState()
    # Example: two players heads-up
    state.players["player1"] = PlayerState(position="SB", stack=1000)
    state.players["player2"] = PlayerState(position="BB", stack=1000)
    return state


def main(video_source: int | str = 0, iterations: int = 1000):
    game_state = setup_game()
    trainer = CFRTrainer()
    trainer.train(iterations)

    while True:
        frame = grab_frame(video_source)
        detection = detect_cards(frame)
        game_state.update_from_detection(detection)
        action = trainer.get_action()
        print(f"Bot action: {action}")
        game_state.record_action("bot", action)
        time.sleep(1)  # simulate delay between actions


if __name__ == "__main__":
    main()
