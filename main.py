from tester import runTester

#задержка при обновлении экрана, сек
DELAY = 1
#файл с вопросами тестов
file = 'testerQuestions.json'

if __name__ == "__main__":
    runTester(file, DELAY)
