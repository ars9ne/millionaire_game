from .question import Question
import random

class Game:

    def __init__(self):
        self.score = 0
        self.current_question = None
        self.questions = [  # некоторые примеры вопросов
            Question("What is the capital of France?", ["Paris", "Berlin", "Madrid", "Rome"], 0),
            Question("Which animal is known as the King of the Jungle?", ["Elephant", "Lion", "Tiger", "Giraffe"], 1),

        ]

    def load_question(self):
        self.current_question = random.choice(self.questions)

    def check_answer(self, answer_index):
        return self.current_question.correct_answer == answer_index
