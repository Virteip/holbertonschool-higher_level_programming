#!/usr/bin/python3
import unittest
from models.square import Square


class TestsRect(unittest.TestCase):
    def test_rectangle_true_normal_values(self):
        self.assertEqual(Square(1).id, 7)
        self.assertEqual(Square(8, 8).x, 8)
        self.assertEqual(Square(2, 2).y, 0)
        self.assertEqual(Square(8, 8).width, 8)
        self.assertEqual(Square(24, 24).height, 24)
        self.assertEqual(Square(1, 1, 1, 1).id, 1)
        self.assertEqual(Square(8, 1, 1, 1).x, 1)
        self.assertEqual(Square(2, 1, 1, 1).y, 1)
        self.assertEqual(Square(8, 1, 1, 1).width, 8)
        self.assertEqual(Square(24, 1, 1, 1).height, 24)

    def test_rectangle_errors(self):
        f = []
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(AttributeError):
            f.__width
            f.__height
            f.__x
            f.__y
        with self.assertRaises(ValueError):
            Square(-8, 0, -24, 0)
        with self.assertRaises(ValueError):
            Square(0, 0, 0, 0)
        with self.assertRaises(TypeError):
            Square("what", "are", "you", "doing")
