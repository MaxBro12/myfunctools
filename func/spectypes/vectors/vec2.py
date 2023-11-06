from typing import Union

from math import degrees, acos


# ? Вектор с 2мя координатами
class Vec2:
    '''Удобный класс для работы с векторами'''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.__x_norm = 0
        self.__y_norm = 0

    @property
    def length(self):
        """Длинна вектора"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @property
    def norm(self):
        """Возвращает нормализованный вектор"""
        if self.length == 0:
            return Vec2(self.__x_norm, self.__y_norm)
        else:
            self.__x_norm = self.x / self.length
            self.__y_norm = self.y / self.length
            return Vec2(self.__x_norm, self.__y_norm)

    @property
    def angle(self):
        """Угол между текущим вектором и базовым вектором Vec2(1, 0)"""
        return acos(dot2(self.norm, Vec2(1, 0)) / self.norm.length * 1) \
            if self.length != 0 else 0

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) == Vec2:
            return Vec2(self.x * other.x, self.y * other.y)
        elif type(other) == Union[int, float]:
            return Vec2(self.x * other, self.y * other)

    def __div__(self, other):
        if type(other) == Vec2:
            return Vec2(self.x / other.x, self.y / other.y)
        elif type(other) == Union[int, float]:
            return Vec2(self.x / other, self.y / other)

    def __getitem__(self, pos: int):
        return (self.x, self.y)[pos]

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


# ? Функция расчета нормализированного вектора 2
def norm2(vec2: Vec2) -> tuple:
    '''Возвращает нормализованный вектор'''
    m = length2(vec2)
    return vec2.x / m, vec2.y / m


# ? Функция расчета длинны вектора 2
def length2(vec2: Vec2) -> Union[float, int]:
    '''Возвращает длинну вектора'''
    return (vec2.x**2 + vec2.y**2)**0.5


# ? Функция расчета сколярного произведения вектора 2
def dot2(a: Vec2, b: Vec2) -> Union[float, int]:
    '''Возвращает скалярное произведение векторов'''
    return a.x * b.x + a.y * b.y


# ? Функция расчета угла между 2мя векторами
def abtv2(a: Vec2, b: Vec2) -> int:
    """Расчитывает угол 2х векторов. Ответ в радианах!"""
    a, b = a.norm, b.norm
    return acos(dot2(a, b) / a.length * b.length)
