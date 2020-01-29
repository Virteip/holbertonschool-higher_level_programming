#!/usr/bin/python3
"""
Test Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestsRect(unittest.TestCase):
    """Class TEstRect"""
    def test_rectangle_true_normal_values(self):
        """test true"""
        self.assertEqual(Rectangle(1, 1).id, 2)
        self.assertEqual(Rectangle(8, 8).x, 0)
        self.assertEqual(Rectangle(2, 2).y, 0)
        self.assertEqual(Rectangle(8, 8).width, 8)
        self.assertEqual(Rectangle(24, 24).height, 24)
        self.assertEqual(Rectangle(1, 1, 1, 1, 1).id, 1)
        self.assertEqual(Rectangle(8, 8, 1, 1, 1).x, 1)
        self.assertEqual(Rectangle(2, 2, 1, 1, 1).y, 1)
        self.assertEqual(Rectangle(8, 8, 1, 1, 1).width, 8)
        self.assertEqual(Rectangle(24, 24, 1, 1, 1).height, 24)

    def test_rectangle_errors(self):
        """test false"""
        f = []
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(AttributeError):
            f.__width
            f.__height
            f.__x
            f.__y
        with self.assertRaises(ValueError):
            Rectangle(-8, 0, -24, 0)
        with self.assertRaises(ValueError):
            Rectangle(0, 0, 0, 0)
        with self.assertRaises(TypeError):
            Rectangle("what", "are", "you", "doing")
