import pytest

from calculator import Calculator

class TestCalulator:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(3, 7) == 10

    def test_subtraction_success(self):
        assert self.calc.subtraction(5, 2) == 3

    def test_division_success(self):
        assert self.calc.division(8, 4) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(3, 2) == 6

    def teardown(self):
        print('Выполнение метода Teardown')