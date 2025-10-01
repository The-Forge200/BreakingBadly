import unittest
from tobuild import count_words, pascals_triangle_row, calculator, reverse_words, factorial


# ============================================================================
# FUNCTIONS TO TEST (Corrected versions)
# ============================================================================

def count_words(text):
    """Count the frequency of each word in a string (case-insensitive)."""
    text = text.lower()
    words = text.split()
    words_count = {}
    
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    
    return words_count


def pascals_triangle_row(n: int) -> list[int]:
    """Return the last row of Pascal's Triangle of height n."""
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        row = [1]
        for k in range(1, n + 1):
            coeff = row[k - 1] * (n - k + 1) // k
            row.append(coeff)
        return row


def calculator(a: float, b: float, op: str) -> float:
    """Perform basic arithmetic operations."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    else:    
        raise ValueError("Invalid operator. Use one of '+', '-', '*', '/'.")


def reverse_words(text: str) -> str:
    """Reverse the order of words in a string."""
    words = text.split()
    return " ".join(reversed(words))


def factorial(n: int) -> int:
    """Compute the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# ============================================================================
# TEST CLASSES
# ============================================================================

class TestCountWords(unittest.TestCase):
    """Test suite for count_words function."""
    
    def test_basic_count(self):
        """Test basic word counting."""
        result = count_words("hello world")
        expected = {"hello": 1, "world": 1}
        self.assertEqual(result, expected)
    
    def test_case_insensitive(self):
        """Test that counting is case-insensitive."""
        result = count_words("Hello hello HELLO")
        expected = {"hello": 3}
        self.assertEqual(result, expected)
    
    def test_multiple_words(self):
        """Test counting with repeated words."""
        result = count_words("the quick brown fox jumps over the lazy dog")
        self.assertEqual(result["the"], 2)
        self.assertEqual(result["quick"], 1)
    
    def test_empty_string(self):
        """Test with empty string."""
        result = count_words("")
        expected = {}
        self.assertEqual(result, expected)
    
    def test_single_word(self):
        """Test with single word."""
        result = count_words("hello")
        expected = {"hello": 1}
        self.assertEqual(result, expected)
    
    def test_multiple_spaces(self):
        """Test handling of multiple spaces between words."""
        result = count_words("hello    world")
        expected = {"hello": 1, "world": 1}
        self.assertEqual(result, expected)


class TestPascalsTriangleRow(unittest.TestCase):
    """Test suite for pascals_triangle_row function."""
    
    def test_row_zero(self):
        """Test the 0th row."""
        result = pascals_triangle_row(0)
        expected = [1]
        self.assertEqual(result, expected)
    
    def test_row_one(self):
        """Test the 1st row."""
        result = pascals_triangle_row(1)
        expected = [1, 1]
        self.assertEqual(result, expected)
    
    def test_row_two(self):
        """Test the 2nd row."""
        result = pascals_triangle_row(2)
        expected = [1, 2, 1]
        self.assertEqual(result, expected)
    
    def test_row_four(self):
        """Test the 4th row (from docstring example)."""
        result = pascals_triangle_row(4)
        expected = [1, 4, 6, 4, 1]
        self.assertEqual(result, expected)
    
    def test_row_five(self):
        """Test the 5th row."""
        result = pascals_triangle_row(5)
        expected = [1, 5, 10, 10, 5, 1]
        self.assertEqual(result, expected)
    
    def test_row_length(self):
        """Test that row length equals n + 1."""
        for n in range(10):
            result = pascals_triangle_row(n)
            self.assertEqual(len(result), n + 1)
    
    def test_row_symmetry(self):
        """Test that rows are symmetric."""
        for n in range(10):
            result = pascals_triangle_row(n)
            self.assertEqual(result, result[::-1])
    
    def test_row_starts_and_ends_with_one(self):
        """Test that every row starts and ends with 1."""
        for n in range(10):
            result = pascals_triangle_row(n)
            self.assertEqual(result[0], 1)
            self.assertEqual(result[-1], 1)


class TestCalculator(unittest.TestCase):
    """Test suite for calculator function."""
    
    def test_addition_positive(self):
        """Test addition with positive numbers."""
        result = calculator(5, 3, "+")
        self.assertEqual(result, 8)
    
    def test_addition_negative(self):
        """Test addition with negative numbers."""
        result = calculator(-5, -3, "+")
        self.assertEqual(result, -8)
    
    def test_addition_mixed(self):
        """Test addition with mixed sign numbers."""
        result = calculator(5, -3, "+")
        self.assertEqual(result, 2)
    
    def test_subtraction(self):
        """Test subtraction."""
        result = calculator(10, 3, "-")
        self.assertEqual(result, 7)
    
    def test_subtraction_negative_result(self):
        """Test subtraction resulting in negative."""
        result = calculator(3, 10, "-")
        self.assertEqual(result, -7)
    
    def test_multiplication(self):
        """Test multiplication."""
        result = calculator(4, 5, "*")
        self.assertEqual(result, 20)
    
    def test_multiplication_by_zero(self):
        """Test multiplication by zero."""
        result = calculator(100, 0, "*")
        self.assertEqual(result, 0)
    
    def test_division(self):
        """Test division."""
        result = calculator(10, 2, "/")
        self.assertEqual(result, 5)
    
    def test_division_float_result(self):
        """Test division with float result."""
        result = calculator(10, 3, "/")
        self.assertAlmostEqual(result, 3.333333, places=5)
    
    def test_division_by_zero(self):
        """Test that division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculator(10, 0, "/")
        self.assertIn("Division by zero", str(context.exception))
    
    def test_invalid_operator(self):
        """Test that invalid operator raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculator(5, 3, "%")
        self.assertIn("Invalid operator", str(context.exception))
    
    def test_another_invalid_operator(self):
        """Test with another invalid operator."""
        with self.assertRaises(ValueError):
            calculator(5, 3, "^")
    
    def test_addition_floats(self):
        """Test with float inputs."""
        result = calculator(5.5, 2.3, "+")
        self.assertAlmostEqual(result, 7.8, places=10)


class TestReverseWords(unittest.TestCase):
    """Test suite for reverse_words function."""
    
    def test_basic_reverse(self):
        """Test basic word reversal."""
        result = reverse_words("the quick brown fox")
        expected = "fox brown quick the"
        self.assertEqual(result, expected)
    
    def test_single_word(self):
        """Test with single word."""
        result = reverse_words("hello")
        expected = "hello"
        self.assertEqual(result, expected)
    
    def test_two_words(self):
        """Test with two words."""
        result = reverse_words("hello world")
        expected = "world hello"
        self.assertEqual(result, expected)
    
    def test_empty_string(self):
        """Test with empty string."""
        result = reverse_words("")
        expected = ""
        self.assertEqual(result, expected)
    
    def test_multiple_spaces(self):
        """Test that multiple spaces are normalized."""
        result = reverse_words("hello    world")
        expected = "world hello"
        self.assertEqual(result, expected)
    
    def test_leading_trailing_spaces(self):
        """Test with leading and trailing spaces."""
        result = reverse_words("  hello world  ")
        expected = "world hello"
        self.assertEqual(result, expected)
    
    def test_preserves_word_content(self):
        """Test that words themselves are not reversed."""
        result = reverse_words("abc def ghi")
        self.assertIn("abc", result)
        self.assertIn("def", result)
        self.assertIn("ghi", result)


class TestFactorial(unittest.TestCase):
    """Test suite for factorial function."""
    
    def test_factorial_zero(self):
        """Test factorial of 0."""
        result = factorial(0)
        self.assertEqual(result, 1)
    
    def test_factorial_one(self):
        """Test factorial of 1."""
        result = factorial(1)
        self.assertEqual(result, 1)
    
    def test_factorial_five(self):
        """Test factorial of 5 (from docstring)."""
        result = factorial(5)
        self.assertEqual(result, 120)
    
    def test_factorial_two(self):
        """Test factorial of 2."""
        result = factorial(2)
        self.assertEqual(result, 2)
    
    def test_factorial_three(self):
        """Test factorial of 3."""
        result = factorial(3)
        self.assertEqual(result, 6)
    
    def test_factorial_ten(self):
        """Test factorial of 10."""
        result = factorial(10)
        self.assertEqual(result, 3628800)
    
    def test_negative_number(self):
        """Test that negative numbers raise ValueError."""
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertIn("negative", str(context.exception).lower())
    
    def test_negative_five(self):
        """Test another negative number."""
        with self.assertRaises(ValueError):
            factorial(-5)
    
    def test_large_factorial(self):
        """Test with a larger number to ensure no overflow."""
        result = factorial(20)
        expected = 2432902008176640000
        self.assertEqual(result, expected)


# ============================================================================
# RUN TESTS
# ============================================================================

if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)