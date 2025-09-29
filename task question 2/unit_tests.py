import unittest
import math
from geometric_shapes import Circle, Triangle, Rectangle, calculate_area

class TestGeometry(unittest.TestCase):
    
    def test_circle_area(self):
        """Тест площади круга радиуса 5"""
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25,
                               "Площадь круга радиуса 5 должна быть 25*Pi")
    
    def test_circle_invalid_radius(self):
        """Тест валидности круга"""
        circle = Circle(-1)
        self.assertFalse(circle.is_valid(),
                         "Круг с отрицательным радиусом должен быть невалидным")
        with self.assertRaises(ValueError):
            circle.area()

    def test_triangle_areas_multiple_cases(self):
        """Тест площади треугольника с несколькими наборами данных"""
        test_cases = [
            (3, 4, 5, 6.0),      # прямоугольный треугольник
            (5, 5, 5, 10.825317547305483),  # равносторонний
            (7, 8, 9, 26.832815729997478),  # произвольный треугольник
            (6, 8, 10, 24.0),    # прямоугольный треугольник
            (2, 3, 4, 2.9047375096555625)   # произвольный треугольник
        ]
        
        for a, b, c, expected_area in test_cases:
            with self.subTest(a=a, b=b, c=c, expected=expected_area):
                triangle = Triangle(a, b, c)
                self.assertAlmostEqual(triangle.area(), expected_area,
                                       f"Площадь треугольника ({a}, {b}, {c}) должна быть {expected_area}")

    def test_triangle_validity_multiple_cases(self):
        """Тест валидности треугольника с несколькими наборами данных"""
        valid_cases = [
            (3, 4, 5),
            (5, 5, 5),
            (7, 8, 9),
            (2, 3, 4)
        ]
        
        invalid_cases = [
            (1, 1, 3),  # нарушение неравенства треугольника
            (0, 2, 3),  # нулевая сторона
            (-1, 2, 3), # отрицательная сторона
            (1, 2, 0)   # нулевая сторона
        ]
        
        for a, b, c in valid_cases:
            with self.subTest(a=a, b=b, c=c, expected_valid=True):
                triangle = Triangle(a, b, c)
                self.assertTrue(triangle.is_valid(),
                               f"Треугольник ({a}, {b}, {c}) должен определяться как существующий")
        
        for a, b, c in invalid_cases:
            with self.subTest(a=a, b=b, c=c, expected_valid=False):
                triangle = Triangle(a, b, c)
                self.assertFalse(triangle.is_valid(),
                                f"Треугольник ({a}, {b}, {c}) должен определяться как НЕсуществующий")

    def test_right_triangle_multiple_cases(self):
        """Тест прямоугольности треугольника с несколькими наборами данных"""
        right_triangles = [
            (3, 4, 5),
            (6, 8, 10),
            (5, 12, 13),
            (7, 24, 25)
        ]
        
        non_right_triangles = [
            (5, 5, 5),
            (7, 8, 9),
            (2, 3, 4),
            (4, 5, 6)
        ]
        
        for a, b, c in right_triangles:
            with self.subTest(a=a, b=b, c=c, expected_right=True):
                triangle = Triangle(a, b, c)
                self.assertTrue(triangle.is_right_triangle(),
                               f"Треугольник ({a}, {b}, {c}) должен быть прямоугольным")
        
        for a, b, c in non_right_triangles:
            with self.subTest(a=a, b=b, c=c, expected_right=False):
                triangle = Triangle(a, b, c)
                self.assertFalse(triangle.is_right_triangle(),
                                f"Треугольник ({a}, {b}, {c}) НЕ должен быть прямоугольным")
    
    def test_calculate_area_polymorphism(self):
        """Тест вычисления площади без знания типа фигуры"""
        circle = Circle(2)
        triangle = Triangle(3, 4, 5)
        
        # Одна функция работает с разными типами фигур
        self.assertAlmostEqual(calculate_area(circle), math.pi * 4,
                              "Площадь круга радиуса 2 через полиморфизм должна быть 4*Pi")
        self.assertAlmostEqual(calculate_area(triangle), 6.0,
                              "Площадь треугольника (3, 4, 5) через полиморфизм должна быть 6.0")
    
    def test_new_shape_extension(self):
        """Тест легкости добавления новых фигур"""
        rectangle = Rectangle(4, 5)
        self.assertAlmostEqual(calculate_area(rectangle), 20.0,
                              "Площадь прямоугольника 4x5 должна быть 20.0")

if __name__ == '__main__':
    unittest.main()