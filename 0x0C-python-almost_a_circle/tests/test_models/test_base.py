#!/usr/bin/python3
import unittest
from models.base import Base


class TestStringMethods(unittest.TestCase):
    def test_id_true(self):
        self.assertEqual(Base(24).id, 24)
        self.assertEqual(Base(2).id, 2)
        self.assertEqual(Base(None).id, 1)
        self.assertEqual(Base('8').id, '8')

    def test_id_errors(self):
        with self.assertRaises(TypeError):
            Base(1, 1)
        with self.assertRaises(AttributeError):
            self.__nb_objects
        self.assertRaises(TypeError, Base, exact=0)
