"""Нужно сделать класс фигур (прямоугольник круг треугольник ) каждый из них будет принимать параметры
необходимые для описания фигуры например длинны сторон или радиус для круга
и каждому определить метод square который будет находить площадь фигуры
и потом сделать функцию которая будет принимать список фигур и находить их общую площадь"""

from math import pi
from math import sqrt


class Figure:
    def __init__(self):
        pass

    def square(self):
        pass


class Triangular(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.p = (self.side_a + self.side_b + self.side_c)/2

    def square(self):
        """Формула Герона: p - полупериметр; s = sqrt(p * (p - a) * (p - b) * (p - c))"""
        return sqrt(self.p * (self.p - self.side_a) * (self.p - self.side_b) * (self.p - self.side_c))


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return pi * (self.radius**2)


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length, self.width = length, width

    def square(self):
        return self.length * self.width


def sum_of_squares(*args):
    return sum([figure.square() for figure in args])


a = Triangular(3, 4, 5)
b = Circle(3)
c = Rectangle(4, 7)

print(a.square(), b.square(), c.square())   #--> 6.0 28.274333882308138 28
print(sum_of_squares(a, b, c, a))   # --> 68.27433388230814