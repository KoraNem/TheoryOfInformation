"""
ОЦІНКА ЕФЕКТИВНОСТІ АЛГОРИТМУ КОДУВАННЯ

ВХІДНІ ДАНІ:
- список з частотами появи літер в тексті
- довжини кодових слів

ВИХІДНІ ДАНІ:
- середня довжина
- ентропія
- ефективність
- стиснення

ФУНКЦІЇ:
Обчислення:
    average_length - обчислення середньої довжини кодових слів
    entropy - обчислення ентропії
    efficiency - оцінка ефективності кодування, використовуються попередні функції
    compression - розрахунок коефіцієнту стиснення
Видача інформації:
    efficiency_rate - інформація про ефективність кодування
    predefined - обчислення ефективності для даних, прописаних в програмі
    manual - введення даних вручну
"""


from math import log2


# ручне введення
probability = [5,3,3,2,2,2,2,2,1,1,1,1]
lengths =     [3,3,3,3,4,4,3,4,4,5,5,4]
base_of_encoding = 2


def average_length(frequency, length):
    return sum(frequency[i] * length[i] for i in range(len(frequency))) / sum(frequency)


def entropy(frequency):
    return -1 * sum(frequency[i] * log2(frequency[i]/sum(frequency)) for i in range(len(frequency))) / sum(frequency)


def efficiency(entropy_value, aver_length, base=2):
    return entropy_value / aver_length / log2(base)


def compression(alphabet_length, aver_length, base=2):
    return log2(alphabet_length) / aver_length / log2(base)


def efficiency_rate(frequency, length, base=2):
    # обраховує, відображує та повертає параметри
    av_len = average_length(frequency, length)
    ent = entropy(frequency)
    eff = efficiency(ent, av_len, base)
    comp = compression(len(frequency), av_len, base)
    return 'Середня довжина: {}\nЕнтропія: {}\nЕфективність: {}\nСтиснення {}'.format(av_len, ent, eff, comp)


def predefined():
    """Дані вже прописані в програмі"""
    try:
        print(efficiency_rate(probability, lengths, base_of_encoding))
    except:
        print('Схоже, щось не так із вхідними даними')


def manual():
    """Вводиться вручну"""
    symbols = list(input('Список символів, що кодуються (все разом): '))
    probability = [int(i) for i in input('Ймовірності появи символів (через пробіл): ').split(' ')]
    lengths = [int(i) for i in input('Довжини закодованих слів (через пробіл): ').split(' ')]
    if len(symbols) == len(probability) == len(lengths):
        print(efficiency_rate(probability, lengths))
    else:
        print('Схоже, щось не так зі вхідними даними')


if __name__ == "__main__":
    if int(input('Дані вже задані? (1-так, 2-ні): ')) == 1:
        predefined()
    else:
        manual()
