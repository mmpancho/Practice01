"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
import random

random.seed(2024)

def game_core_v3(number: int = 1) -> int:
    """Функция, которая угадывает случайное число от 1 до 100 за минимальное число попыток.
    Возвращает количество попыток, за которые число было угадано.
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """    
    # Ваш код начинается здесь
    low = 1
    high = 100
    count = 0

    while True:
        count += 1
        predict = (low + high) // 2

        if predict == number:
            return count
        elif predict < number:
            low = predict + 1
        else:
            high = predict - 1
    # Ваш код заканчивается здесь

    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(2024)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)