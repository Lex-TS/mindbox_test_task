import math
from abc import ABC, abstractmethod

class Shape(ABC):
    """Абстрактный базовый класс для всех фигур"""
    
    @abstractmethod
    def is_valid(self) -> bool:
        """Проверяет, может ли фигура существовать с заданными параметрами"""
        pass

    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры"""
        pass

class Circle(Shape):
    """Класс для работы с кругом"""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def is_valid(self) -> bool:
        """Проверяет корректность радиуса"""
        return self.radius > 0
    
    def area(self) -> float:
        """Вычисляет площадь круга: pi * r^2"""
        if not self.is_valid():
            raise ValueError("Некорректный радиус круга")
        return math.pi * self.radius ** 2

class Triangle(Shape):
    """Класс для работы с треугольником"""

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        """Проверяет неравенство треугольника"""
        sides = sorted([self.a, self.b, self.c])  # Упорядочиваем по возрастанию
        return (all(s > 0 for s in sides) and
            sides[0] + sides[1] > sides[2])   # Проверяем только одну комбинацию

    def area(self) -> float:
        """Вычисляет площадь по формуле Герона"""
        if not self.is_valid():
            raise ValueError("Треугольник с такими сторонами не существует")
        
        p = (self.a + self.b + self.c) / 2  # полупериметр
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    def is_right_triangle(self) -> bool:
        """Проверяет, является ли треугольник прямоугольным"""
        if not self.is_valid():
            return False
        
        sides = sorted([self.a, self.b, self.c]) # сторона sides[2] будет наибольшей 
        # Проверяем теорему Пифагора: a^2 + b^2 = c^2
        return sides[0]**2 + sides[1]**2 == sides[2]**2

def calculate_area(shape: Shape) -> float:
    """Вычисляет площадь фигуры без знания её типа в compile-time"""
    return shape.area()

# Пример добавления новой фигуры (для демонстрации расширяемости)
class Rectangle(Shape):
    """Пример добавления новой фигуры - прямоугольника"""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def is_valid(self) -> bool:
        return self.width > 0 and self.height > 0
    
    def area(self) -> float:
        if not self.is_valid():
            raise ValueError("Некорректные размеры прямоугольника")
        return self.width * self.height