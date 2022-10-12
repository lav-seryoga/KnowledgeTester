from random import shuffle
import json

class LoadJsonFile:

    def __init__(self, json_file) -> None:
        """
        принимает файл формата json
        выполняет парсинг файла
        """

        self.json_file = json_file
        with open(self.json_file, 'r', encoding='utf-8') as file:
            self.tests = json.load(file)

    def formListOfTests(self):
        """
        формирует список с тестами,
        тесты сортируются в случайном порядке
        """

        list = []
        for elem in self.tests:
            list.append(elem)

        shuffle(list)

        return list

class ExecuteOperation:

    def __init__(self, test) -> None:
        """
        принимает объект типа test,
        формирует список с вариантами ответов и перетасовывает его
        """

        self.test = test
        self.options = []
        
        for elem in self.test['options']:
            self.options.append(elem)

        shuffle(self.options)

    def showTestInputAnswer(self, qIndex):
        """
        принимает порядковый номер вопроса
        подготавливает словарь с вариантами ответов, где ключ - индекс, а значение - вариант ответа
        выводит на экран вопрос и варианты ответов
        считывает ответ пользователя
        """

        self.variants = {}
        
        index = ord("а")
        for elem in self.options:
            self.variants[chr(index)] = elem
            index += 1

        print(f"\nВопрос {qIndex}. {self.test['question']}")
        
        dash = []
        for i in self.test['question']:
            dash.append("-")
        print("".join(dash))

        for key, value in self.variants.items():
            print(f"{key}. {value}")

        self.answer = input(f"Укажите номер правильного ответа (a-{chr(index-1)}): ")
        
    def compareAnswer(self):
        """
        сравнивает ответ c верным вариантом
        возвращает Истина, если ответы совпали, иначе - Ложь
        """

        return True if self.variants[self.answer] == self.test["answer"][0] else False