from testOperations import LoadJsonFile
from testOperations import ExecuteOperation as prepareTest

import os
import time

def clscr():
    """
    очищает экран
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def runTester(file, delay):
    """
    получает файла формата json и значение задержки экрана в сек.
    """
    questionsQuantity = 0
    answersQuantity = 0

    listOfTests = LoadJsonFile(file).formListOfTests()

    for elem in listOfTests:
        clscr()
        
        test = prepareTest(elem)
        
        try:
            questionsQuantity += 1
            
            test.showTestInputAnswer(questionsQuantity)

            if test.compareAnswer():
                answersQuantity += 1
                print("\nЭто правильный ответ!")
            else:
                print("\nЭто неправильный ответ!")
            
            time.sleep(delay)
    
        except KeyError:
            print("\nПовторите ввод")
            time.sleep(delay)
            clscr()
            
            isError = True
            while isError:
                try:
                    test.showTestInputAnswer(questionsQuantity)

                    if test.compareAnswer():
                        answersQuantity += 1
                        print("\nЭто правильный ответ!")
                        time.sleep(delay)
                        clscr()
                    else:
                        print("\nЭто неправильный ответ!")
                        time.sleep(delay)

                    isError = False

                except KeyError:
                    print("\nПовторите ввод")
                    time.sleep(delay)
                    clscr()

    print(f"\nВаша оценка: {answersQuantity} верных ответов из {questionsQuantity} \n")