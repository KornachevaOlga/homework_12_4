import unittest
import logging
from rt_with_exceptions import Runner, Tournament
from unittest import TestCase

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')


# Название файла - runner_tests.log
# Кодировка - UTF-8

class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test_walk(self):
        try:
            runner = Runner("John", -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
        except ValueError as exc:
            logging.warning('Некорректная скорость', exc_info=exc)

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test_run(self):
        try:
            runner = Runner(2)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except TypeError as exc:
            logging.warning('Некорректный результат', exc_info=exc)

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test_challenge(self):
        runner1 = Runner("John")
        runner2 = Runner("Jane")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


# Задача:

class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        TournamentTest.all_results[1] = result
        self.assertTrue(result[2] == "Ник")

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        TournamentTest.all_results[2] = result
        self.assertTrue(result[2] == "Ник")

    @unittest.skipIf(is_frozen, 'Тест заморожен')
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament.start()
        TournamentTest.all_results[3] = result
        self.assertTrue(result[3] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

# Задача "Логирование бегунов":

# Дополните методы тестирования в классе RunnerTest следующим образом:
# test_walk:
# Оберните основной код конструкцией try-except.
# При создании объекта Runner передавайте отрицательное значение в speed.
# В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
# В блоке except обработайте исключение соответствующего типа и логируйте его на уровне
# WARNING с сообщением "Неверная скорость для Runner".
# test_run:
# Оберните основной код конструкцией try-except.
# При создании объекта Runner передавайте что-то кроме строки в name.
# В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
# В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".
# Пример результата выполнения программы: