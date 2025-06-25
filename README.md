# Poker Bot

This repository contains a minimal framework for building a Texas Hold'em poker bot using
computer vision and game-theoretic decision making. The project shows how to capture
video frames, detect playing cards, maintain a structured game state, and select
actions using a simplified Counterfactual Regret Minimization (CFR) trainer.

## Structure

```
README.md               - This file
poker_bot/
    requirements.txt    - Python package requirements
    vision.py           - Vision utilities (frame capture and card detection)
    state.py            - Data structures representing game state
    cfr.py              - Simplified CFR implementation
    main.py             - Example integration loop
```

## Setup

1. Install Python 3.10 or newer.
2. Create a virtual environment and install requirements:

```bash
python -m venv venv
source venv/bin/activate
pip install -r poker_bot/requirements.txt
```

3. Set up OpenAI API credentials if you plan to use the vision API. The current
   implementation includes a placeholder in `vision.py` where API calls should be
   added.

## Running

The main entry point is `poker_bot/main.py`.

```bash
python poker_bot/main.py
```

By default, the script trains a simple CFR model and then enters an infinite loop
where it captures frames, parses detections, and prints the chosen action every
second. Replace the placeholder detection logic with calls to your computer vision
backend to make it fully functional.

## Evaluating the Bot

To evaluate performance, you can pit the bot against baseline strategies such as
random play or simple rule-based opponents. Compare win rates over many hands and
observe decision quality in various situations. For rigorous evaluation, integrate
a poker simulator that supports automated play and record statistics like expected
value, fold equity, and exploitability.
