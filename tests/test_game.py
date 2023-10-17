# tests/test_game.py

import unittest
from game.game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_game_initialization(self):
        self.assertEqual(self.game.score, 0)
        self.assertIsNone(self.game.current_question)

    def test_load_question(self):
        self.game.load_question()
        self.assertIsNotNone(self.game.current_question)

    def test_check_answer(self):
        self.game.current_question = ("What is the capital of France?", ["Paris", "Berlin", "Madrid", "Rome"], 0)
        self.assertTrue(self.game.check_answer(0))
        self.assertFalse(self.game.check_answer(1))
