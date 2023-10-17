class Question:

    def __init__(self, question, options, correct_answer):
        """
        Конструктор класса Question.

        :param question: str - текст вопроса.
        :param options: list - список из четырех вариантов ответа.
        :param correct_answer: int - индекс правильного ответа в списке options (0-3).
        """
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def display(self):
        """
        Отображение вопроса и вариантов ответа.
        """
        print(self.question)
        for idx, option in enumerate(self.options):
            print(f"{idx}. {option}")

    def is_correct(self, answer_index):
        """
        Проверка, является ли данный индекс правильным ответом.

        :param answer_index: int - индекс выбранного ответа.
        :return: bool - True, если ответ верный, иначе False.
        """
        return self.correct_answer == answer_index
