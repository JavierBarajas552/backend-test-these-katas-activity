import unittest
import katas
import math
import random


class TestKatas(unittest.TestCase):
    def test_add(self):
        first = int(math.floor(random.random()*100))
        second = int(math.floor(random.random()*100))
        test = katas.add(first, second)
        self.assertEqual(first + second, test)

    def test_multiply(self):
        first = int(math.floor(random.random()*100))
        second = int(math.floor(random.random()*100))
        test = katas.multiply(first, second)
        self.assertEqual(first * second, test)

    def test_power(self):
        first = int(math.floor(random.random()*100))
        second = int(math.floor(random.random()*100))
        test = katas.power(first, second)
        self.assertEqual(first ** second, test)

    def test_factorial(self):
        first = int(math.floor(random.random()*100))
        test = katas.factorial(first)
        self.assertEqual(math.factorial(first), test)

    def test_fibonacci(self):
        fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        first = int(math.floor(random.random()*10))
        test = katas.fibonacci(first+1)
        self.assertEqual(fib[first], test)


if __name__ == '__main__':
    unittest.main()
