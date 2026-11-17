import unittest

from Pac_man import Score, replay


class ReplayTests(unittest.TestCase):
    def test_bonus_life_does_not_change_score(self):
        self.assertEqual(replay(['Key', 'Dot']), Score(10010, 4, 2))

    def test_ghost_chain_and_death(self):
        ghosts = ['VulnerableGhost'] * 4
        self.assertEqual(replay(ghosts), Score(8000, 3, 4))
        self.assertEqual(replay(['InvincibleGhost'] * 3 + ['Key']), Score(5000, 0, 3))

    def test_unrecognized_event(self):
        with self.assertRaises(ValueError):
            replay(['Unknown'])
