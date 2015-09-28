# coding: UTF-8

from unittest import TestCase
from ex3 import min


class Ex3Test(TestCase):
    def test_min(self):
        self.assertEqual(1, min([100, 20, 5, 1, 200, 5]))