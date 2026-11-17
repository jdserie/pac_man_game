"""Replay a sequence of events from the original arcade scoring exercise."""
import argparse
from dataclasses import dataclass
from pathlib import Path

POINTS = {
    'Dot': 10, 'Cherry': 100, 'Strawberry': 300, 'Orange': 500, 'Apple': 700,
    'Melon': 1000, 'Galaxian': 2000, 'Bell': 3000, 'Key': 5000,
}
GHOST_POINTS = (200, 400, 800, 1600)
EVENTS = {*POINTS, 'VulnerableGhost', 'InvincibleGhost'}


@dataclass(frozen=True)
class Score:
    points: int
    lives: int
    events_played: int


def replay(events):
    points = 5000
    lives = 3
    next_bonus = 10000
    ghosts = 0
    played = 0
    for event in events:
        if event not in EVENTS:
            raise ValueError(f'Unknown event: {event!r}')
        if not lives:
            break
        played += 1
        if event == 'InvincibleGhost':
            lives -= 1
            ghosts = 0
        elif event == 'VulnerableGhost':
            points += GHOST_POINTS[min(ghosts, len(GHOST_POINTS) - 1)]
            ghosts += 1
        else:
            points += POINTS[event]
        while points >= next_bonus:
            lives += 1
            next_bonus += 10000
    return Score(points, lives, played)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', nargs='?', type=Path, default=Path(__file__).with_name('game.txt'))
    parser.add_argument('--details', action='store_true', help='Show remaining lives and events played.')
    args = parser.parse_args()
    try:
        events = [value.strip() for value in args.file.read_text(encoding='utf-8').split(',') if value.strip()]
        score = replay(events)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(score.points)
    if args.details:
        print(f'Lives remaining: {score.lives} · Events played: {score.events_played}')


if __name__ == '__main__':
    main()
