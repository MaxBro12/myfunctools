from typing import Union

from math import degrees, acos


# ? Вектор с 3мя координатами
class Vec3:
    '''Удобный класс для работы с векторами'''
    def __init__(self, x='0', y=0, z=0):
        if type(x) == tuple or type(x) == list:
            self.x = x[0]
            self.y = x[1]
            self.z = x[2]
        else:
            self.x = int(x)
            self.y = y
            self.z = z
        self.__x_norm = 0
        self.__y_norm = 0
        self.__z_norm = 0

    def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    @property
    def norm(self):
        self.__x_norm = self.x / self.length()
        self.__y_norm = self.y / self.length()
        self.__z_norm = self.z / self.length()
        return self.__x_norm, self.__y_norm, self.__z_norm

    def __add__(self, other):
        if type(other) == Vec3:
            return self.x + other.x, self.y + other.y, self.z + other.z
        elif type(other) == tuple or type(other) == list:
            return self.x + other[0], self.y + other[1], self.z + other[2]
        else:
            return self.x + other, self.y + other, self.z + other

    def __sub__(self, other):
        if type(other) == Vec3:
            return self.x - other.x, self.y - other.y, self.z - other.z
        elif type(other) == tuple or type(other) == list:
            return self.x - other[0], self.y - other[1], self.z - other[2]
        else:
            return self.x - other, self.y - other, self.z - other

    def __mul__(self, other):
        if type(other) == Vec3:
            return self.x * other.x, self.y * other.y, self.z * other.z
        elif type(other) == tuple or type(other) == list:
            return self.x * other[0], self.y * other[1], self.z * other[2]
        else:
            return self.x * other, self.y * other, self.z * other

    def __div__(self, other):
        if type(other) == Vec3:
            return self.x / other.x, self.y / other.y, self.z / other.z
        elif type(other) == tuple or type(other) == list:
            return self.x / other[0], self.y / other[1], self.z / other[2]
        else:
            return self.x / other, self.y / other, self.z / other

    def __getitem__(self, pos: int):
        return (self.x, self.y, self.z)[pos]

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}"


# ? Функция расчета нормализированного вектора 3
def norm3(vec3: Vec3) -> tuple:
    '''Возвращает нормализованный вектор'''
    m = length3(vec3)
    return vec3.x / m, vec3.y / m, vec3.z / m


# ? Функция расчета длинны вектора 3
def length3(vec3: Vec3) -> Union[float, int]:
    '''Возвращает длинну вектора'''
    return (vec3.x**2 + vec3.y**2 + vec3.z**2)**0.5


# ? Функция расчета сколярного произведения вектора 3
def dot3(a: Vec3, b: Vec3) -> Union[float, int]:
    '''Возвращает скалярное произведение векторов'''
    return a.x * b.x + a.y * b.y + a.z * b.z
