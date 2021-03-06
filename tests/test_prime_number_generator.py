import unittest

from app.prime_number_generator import generate_primes


class TestPrimeNumberGenerator(unittest.TestCase):

    def test_generator_returns_error_if_both_limits_are_not_numbers(self):
        self.assertRaises(ValueError, generate_primes, 'zero', 'ten')
    
    def test_generator_returns_error_if_lower_limit_is_not_number(self):
        self.assertRaises(ValueError, generate_primes, 2, 'Ten')
    
    def test_generator_returns_error_if_upper_limit_is_not_number(self):
        self.assertRaises(ValueError, generate_primes, 'Two', 10)
    
    def test_generator_returns_error_if_both_limits_are_negative(self):
        self.assertEquals(generate_primes(-1, -10), 
                           "all limit intervals must be positive")

    def test_generator_returns_error_if_lower_limit_is_negative(self):
        self.assertEquals(generate_primes(-1, 10), 
                           "all limit intervals must be positive")

    def test_generator_returns_error_if_upper_limit_is_negative(self):
        self.assertEquals(generate_primes(1, -10), 
                           "all limit intervals must be positive")

    def test_generator_returns_correct_list_of_prime_numbers(self):
        self.assertListEqual(generate_primes(0, 10), [2, 3, 5, 7])

    def test_generator_returns_correct_list2_of_prime_numbers(self):
        self.assertListEqual(generate_primes(10, 30), 
                             [11, 13, 17, 19, 23, 29])


if __name__ == '__main__':
    unittest.main()