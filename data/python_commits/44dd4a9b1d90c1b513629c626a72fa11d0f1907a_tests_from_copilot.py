import unittest
from wordle import Color, Feedback, Attempt, give_feedback, Game

class TestWordle(unittest.TestCase):
    def test_feedback_is_correct(self):
        feedback = Feedback([Color.green, Color.green, Color.green, Color.green, Color.green])
        self.assertTrue(feedback.is_correct())

    def test_attempt_is_correct(self):
        attempt = Attempt('helps', [Color.green, Color.green, Color.green, Color.green, Color.green])
        self.assertTrue(attempt.is_correct())

    def test_give_feedback(self):
        attempt = give_feedback('smile', 'helps')
        self.assertEqual(attempt.feedback, [Color.grey, Color.green, Color.grey, Color.grey, Color.grey])

    def test_game_guess_word(self):
        game = Game('helps')
        attempt = game.guess_word('smile')
        self.assertEqual(attempt.feedback, [Color.grey, Color.green, Color.grey, Color.grey, Color.grey])

    def test_game_n_attempts(self):
        game = Game('helps')
        game.guess_word('smile')
        game.guess_word('tells')
        self.assertEqual(game.n_attempts, 2)

if __name__ == '__main__':
    unittest.main()