#!/usr/bin/python3
"""
Unit Tests
"""
import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for Base module
    """
    def test_bettystyle(self):
        """
        Check PEP8
        """
        betty = pep8.StyleGuide(quiet=True)
        check = betty.check_files(['models/base.py', 'models/rectangle.py',
                                   'models/square.py'])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warnings).")
