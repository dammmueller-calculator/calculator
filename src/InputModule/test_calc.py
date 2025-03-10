import unittest

from InputModule import calc


class TestGermanCalculator(unittest.TestCase):

    # -------------
    # FIRST TABLE
    # -------------
    def test_addition_1_plus_1(self):
        self.assertEqual(calc("1 + 1"), 2)

    def test_addition_long(self):
        self.assertEqual(calc("3 + 5 + 4 + 22 + 155"), 189)

    def test_subtraction_2_minus_1(self):
        self.assertEqual(calc("2 - 1"), 1)

    def test_subtraction_chain(self):
        self.assertEqual(calc("2 - 5 - 3"), -6)

    def test_subtraction_long_chain(self):
        self.assertEqual(calc("100 - 35 - 5 - 10 - 2"), 48)

    def test_division_1_div_2(self):
        # 1/2 should be 0.5 (German: 0,5)
        self.assertAlmostEqual(calc("1 / 2"), 0.5, places=7)

    def test_division_6_div_3(self):
        self.assertEqual(calc("6 / 3"), 2)

    def test_division_by_zero(self):
        # Expect an error or custom handling if 5/0 is "Nicht Lösbar".
        # Here we assume an exception is raised.
        with self.assertRaises(ZeroDivisionError):
            calc("5 / 0")

    def test_division_0_div_1(self):
        self.assertEqual(calc("0 / 1"), 0)

    def test_division_negative(self):
        self.assertEqual(calc("-6 / 3"), -2)

    def test_division_german_decimal(self):
        # "3 / 0,5" => 3 / 0.5 => 6
        self.assertEqual(calc("3 / 0,5"), 6)

    def test_negative_division_german_decimal(self):
        # "-155 / -0,002" => 77500
        self.assertEqual(calc("-155 / -0,002"), 77500)

    def test_fraction_2_div_3(self):
        # Check approximate value 0.6666666667
        self.assertAlmostEqual(calc("2 / 3"), 0.6666666667, places=7)

    def test_multiplication_1_x_6(self):
        self.assertEqual(calc("1 * 6"), 6)

    def test_multiplication_2_x_0(self):
        self.assertEqual(calc("2 * 0"), 0)

    def test_multiplication_66_times_79(self):
        self.assertEqual(calc("66*79"), 5214)

    def test_multiplication_with_zero(self):
        self.assertEqual(calc("66 * 79 * 0"), 0)

    def test_multiplication_german_decimals(self):
        # 2,2 x 3,1 x 17,77 => ~121.1914
        self.assertAlmostEqual(calc("2,2 * 3,1 * 17,77"), 121.1914, places=4)

    def test_multiplication_negatives(self):
        self.assertEqual(calc("-2 * -2"), 4)

    def test_multiplication_negative_positive(self):
        self.assertEqual(calc("-2 * 2"), -4)

    def test_parentheses_simple(self):
        self.assertEqual(calc("1 + (2 + 3)"), 6)

    def test_nested_parentheses(self):
        # 5 - (3 - 2 - (6 - 8)) => 2
        self.assertEqual(calc("5 - (3 - 2 - (6 - 8))"), 2)

    def test_mixed_precedence(self):
        # 3 - 2 x 5 => 3 - 10 => -7
        self.assertEqual(calc("3 - 2 * 5"), -7)

    def test_complex_expression(self):
        # 1 / 0,5 - 3 + 5 * 150 * (-15)
        # 1 / 0.5 => 2 => 2 - 3 => -1 => 5*150 => 750 => 750 * -15 => -11250 => -1 + -11250 => -11251
        self.assertEqual(calc("1 / 0,5 - 3 + 5 * 150 * (-15)"), -11251)

    def test_complex_with_parentheses(self):
        # -(10 + 5) * 15 * (10 / 2 - 3) + 4 => -446
        self.assertEqual(calc("-(10 + 5) * 15 * (10 / 2 - 3) + 4"), -446)

    def test_add_german_decimals(self):
        # 1,2 + 3,5 => 4,7 => 4.7 in standard
        self.assertAlmostEqual(calc("1,2 + 3,5"), 4.7, places=7)

    def test_mixed_german_decimals(self):
        # 0,5 + 1,5 x 2 => 0.5 + (1.5 * 2) => 0.5 + 3 => 3.5
        self.assertAlmostEqual(calc("0,5 + 1,5 * 2"), 3.5, places=7)

    def test_power_operator_caret(self):
        # Test that caret (^) is correctly replaced with ** for exponentiation.
        self.assertEqual(calc("2 ^ 3"), 8)
        self.assertEqual(calc("2 ^ 3 + 4"), 12)
        # Testing right-associativity: 2 ^ 3 ^ 2 => 2 ** (3 ** 2) = 2 ** 9 = 512
        self.assertEqual(calc("2 ^ 3 ^ 2"), 512)

    def test_power_operator_exp(self):
        # Direct use of ** should be handled as well.
        self.assertEqual(calc("2 ** 3"), 8)
        self.assertEqual(calc("2 ** 3 + 4"), 12)
        self.assertEqual(calc("2 ** 3 ** 2"), 512)


# To run the tests:
if __name__ == "__main__":
    unittest.main()
