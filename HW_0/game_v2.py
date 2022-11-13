"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number) -> int:
    
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    predict_number = np.random.randint(1, 101) # загадываем рандомное число, используя генератор рандомных чисел
    count = 0 # Переменная счетчик
    min_num = 1 # Минимальное значение рассматриваемого интервала
    max_num = 100 # Максимальное значение рассматриваемого интервала
    while True:
        count += 1
        if predict_number > number:
            max_num = predict_number - 1
            predict_number = (max_num + min_num) // 2
        elif predict_number < number:
            min_num = predict_number + 1
            predict_number = (max_num + min_num) // 2
        else:
            #print(f'Компьютер угадал загаданное число за {count} попыток. Это число {number}')
            break # конец игры и выход из цикла
    return(count)
# print(f'Количество попыток: {random_predict(number)}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(int(random_predict(number)))
        
    score =int(np.mean(count_ls))
    print(f'ваш алгоритм угадывает в среднем за: {score} попыток')
    return(score)  

#print(f'количество попыток: {random_predict(10)}')   

# RUN
if __name__ == '__main__':
    score_game(random_predict)