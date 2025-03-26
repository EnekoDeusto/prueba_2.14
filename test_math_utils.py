import unittest
import math_utils
from math import sqrt
from math_utils import es_primo


class TestUtils(unittest.TestCase):
    def test_es_primo(self):
        self.assertFalse(es_primo(-5))  # Números negativos no pueden ser primos
        self.assertFalse(es_primo(0))   # 0 no es primo
        self.assertFalse(es_primo(1))   # 1 no es primo
        self.assertTrue(es_primo(2))    # 2 es primo
        self.assertTrue(es_primo(3))    # 3 es primo
        self.assertFalse(es_primo(4))   # 4 no es primo
        self.assertTrue(es_primo(5))    # 5 es primo
        self.assertFalse(es_primo(9))   # 9 no es primo



if __name__ == "__main__":
    unittest.main()
