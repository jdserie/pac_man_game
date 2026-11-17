# Arcade Score Replay

A Python exercise that replays a list of recorded arcade events and calculates a score. Start with 5,000 points and three lives. A collision costs a life, consecutive vulnerable ghosts increase their score award, and the program adds a life at every 10,000-point threshold.

```sh
python Pac_man.py --details
python Pac_man.py game.txt
python -m unittest
```

Input is a comma-separated list of event names. The included `game.txt` is the original sample. This project is a score replay utility.

Joshua Serie's [original March 2019 exercise](https://github.com/jdserie/pac_man_game/commit/1d461370a5bfe8c3ba2a616aaa9cbb478a480143) remains in Git history. The AI-assisted refresh completes the event loop and adds repeatable tests.
