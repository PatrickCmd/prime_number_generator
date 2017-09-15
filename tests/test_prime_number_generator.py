import unittest

from app.prime_number_generator import generate_primes


class TestPrimeNumberGenerator(unittest.TestCase):

    def test_generator_returns_error_if_both_limits_are_not_numbers(self):
        self.assertRaises(ValueError, generate_primes, 'zero', 'ten')
    
    def test_generator_returns_error_if_lower_limit_is_not_number(self):
        self.assertRaises(ValueError, generate_primes, 2, 'Ten')
    
    def test_generator_returns_error_if_upper_limit_is_not_number(self):
        self.assertRaises(ValueError, generate_primes, 'Two', 10)


if __name__ == '__main__':
    unittest.main()