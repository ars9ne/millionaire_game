import unittest
from game.question import Question

class TestQuestion(unittest.TestCase):

    def setUp(self):
        self.sample_question = Question("Что является столицей Франции?", ["Париж", "Берлин", "Мадрид", "Рим"], 0)

    def test_display(self):
        # Проверим, что метод отображает информацию корректно
        self.assertIsNone(self.sample_question.display())

    def test_is_correct(self):
        # Проверка правильного ответа
        self.assertTrue(self.sample_question.is_correct(0))
        # Проверка неправильного ответа
        self.assertFalse(self.sample_question.is_correct(1))

    def test_options_length(self):
        # Проверим, что у нас всегда четыре варианта ответа
        self.assertEqual(len(self.sample_question.options), 4)

    def test_correct_answer_index(self):
        # Проверим, что индекс правильного ответа не выходит за пределы списка вариантов ответа
        self.assertTrue(0 <= self.sample_question.correct_answer < 4)

if __name__ == '__main__':
    unittest.main()