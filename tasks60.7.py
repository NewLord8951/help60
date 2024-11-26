import random


def бросок_двух_кубиков():
    кубик_1 = random.randint(1, 6)
    кубик_2 = random.randint(1, 6)
    сумма = кубик_1 + кубик_2
    return сумма
