from game import Game, Question


def main():
    game = Game()

    print("Добро пожаловать в игру 'Как стать миллионером'!")
    while True:
        game.load_question()
        game.current_question.display()

        try:
            user_answer = int(input("Выберите ваш ответ (0-3): "))
            if user_answer not in [0, 1, 2, 3]:
                raise ValueError

            if game.check_answer(user_answer):
                print("Правильно!")
                game.score += 1
            else:
                print(
                    f"Неверно! Правильный ответ: {game.current_question.options[game.current_question.correct_answer]}")
                break

            continue_game = input("Хотите продолжить игру? (да/нет): ").strip().lower()
            if continue_game == 'нет':
                break

        except ValueError:
            print("Пожалуйста, введите число от 0 до 3.")

    print(f"Ваш итоговый счет: {game.score}")


if __name__ == '__main__':
    main()
