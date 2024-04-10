# для использования аннотаций типов
from typing import Tuple

"""
1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список,
содержащий только уникальные элементы из исходного списка.
"""


def get_unique_elements(lst: list):
    """ Ф-ия для возврата уник.значений списка из вх. данных. """
    # используем множества - set()
    return list(set(lst))


# Пример:
x = [1, 2, 3, 3, 2, 1, 1, 4]
print("1.", get_unique_elements(x))


"""
2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) 
и возвращает список всех простых чисел в заданном диапазоне.
"""
# Простые числа – это числа, которые делятся на себя и на единицу (2, 3, 5, 7 и т.д.)


def is_prime(n: int):
    """ Ф-ия проверяет, является ли число простым. """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes_in_range(min_value: int, max_value: int):
    """ Возвращает список всех простых чисел в заданном диапазоне [min_value, max_value]. """
    return [n for n in range(min_value, max_value + 1) if is_prime(n)]


# Пример:
a, b = 3, 14
print("2.", get_primes_in_range(a, b))


"""
3. Создать класс Point, который представляет собой точку в двумерном пространстве. 
Класс должен иметь методы для инициализации координат точки, вычисления расстояния до другой точки, 
а также для получения и изменения координат.
"""


class Point:
    """ Класс Point представляет точку в двумерном пространстве. """
    def __init__(self, x: float, y: float):
        """ Инициализация координат точки. """
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        """ Ф. вычисляет расстояние от текущей точки до другой точки. """
        # Параметр other должен быть экземпляром класса Point.
        # Возвращает расстояние между точками в виде числа с плавающей точкой (float).

        dx = self.x - other.x  # Разница координат x
        dy = self.y - other.y  # Разница координат y
        # Возвращаем расстояние между точками, вычисленное по формуле Эвклида:
        return (dx**2 + dy**2) ** 0.5

    def get_coordinates(self) -> Tuple[float, float]:
        """ Возвращает кортеж из координат точки (x, y) """
        return self.x, self.y

    def set_coordinates(self, x: float, y: float):
        """Ф. устанавливает новые координаты точки."""
        self.x = x
        self.y = y

# Пример:


point1 = Point(1.05, 4.07)
point2 = Point(6.02, 9.08)

# Вычисляем расстояние между точками
# И округляем результат до 2 знаков после запятой:
distance = round(point1.distance_to(point2), 2)
print(f"3. Расстояние между точками: {distance}")

# Получаем координаты первой точки:
coordinates = point1.get_coordinates()
print(f"Координаты первой точки: {coordinates}")

# Устанавливаем новые координаты первой точки:
point1.set_coordinates(3.14, 2.71)
coordinates = point1.get_coordinates()
print(f"Новые координаты первой точки: {coordinates}")


""" 4. Написать программу, которая сортирует список строк по длине, 
сначала по возрастанию, а затем по убыванию."""


def sort_strings_by_length(strings: list[str]) -> None:
    """ Ф-ия сортировки по длине списка с str-значениями. """
    strings.sort(key=len)
    print("4. Отсортирован по возрастающей длине:", strings)
    strings.sort(key=len, reverse=True)
    print("Отсортирован по убывающей длине:", strings)


# Пример:
strings = ["дом", "авто", "птица", "квартира", "вермишель"]
sort_strings_by_length(strings)
