import unittest
from library_figure import *


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(radius=5)
        expected_area = math.pi * 5 ** 2
        self.assertAlmostEqual(circle.area(), expected_area, places=5)

    def test_triangle_area(self):
        triangle = Triangle(a=3, b=4, c=5)
        expected_area = 6.0
        self.assertAlmostEqual(triangle.area(), expected_area, places=5)

    def test_is_right_triangle(self):
        right_triangle = Triangle(a=3, b=4, c=5)
        non_right_triangle = Triangle(a=5, b=5, c=5)
        self.assertTrue(right_triangle.is_right_triangle())
        self.assertFalse(non_right_triangle.is_right_triangle())

    def test_invalid_triangle_creation(self):
        with self.assertRaises(ValueError):
            invalid_triangle = Triangle(a=1, b=2, c=3)

if __name__ == '__main__':
    unittest.main()