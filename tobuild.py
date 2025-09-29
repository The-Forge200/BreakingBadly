"""
BreakItTillYouMakeIt - Text & Math Utility Functions
Author: Your Name
Instructions: Implement each function below according to the docstrings.
Then write unit tests to verify correctness.
"""

def count_words(text: str) -> dict:
    """
    Count the frequency of each word in a string (case-insensitive).

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary where keys are words and values are counts.

    Examples:
        count_words("Hello hello world") -> {"hello": 2, "world": 1}
    """
    raise NotImplementedError("Implement count_words function")


def pascals_triangle_row(n: int) -> list[int]:
    """
    Return the last row of Pascal's Triangle of height n.

    Args:
        n (int): Height of the triangle (0-indexed).

    Returns:
        list[int]: List representing the last row.

    Examples:
        pascals_triangle_row(4) -> [1, 4, 6, 4, 1]
    """
    raise NotImplementedError("Implement pascals_triangle_row function")


def calculator(a: float, b: float, op: str) -> float:
    """
    Perform basic arithmetic operations.

    Args:
        a (float): First number.
        b (float): Second number.
        op (str): Operator, one of "+", "-", "*", "/".

    Returns:
        float: Result of the operation.

    Raises:
        ValueError: If division by zero is attempted.

    Examples:
        calculator(5, 3, "+") -> 8
        calculator(10, 2, "/") -> 5
    """
    raise NotImplementedError("Implement calculator function")


def reverse_words(text: str) -> str:
    """
    Reverse the order of words in a string (words themselves unchanged).

    Args:
        text (str): Input string.

    Returns:
        str: Words reversed.

    Examples:
        reverse_words("the quick brown fox") -> "fox brown quick the"
    """
    raise NotImplementedError("Implement reverse_words function")


def factorial(n: int) -> int:
    """
    Compute the factorial of a non-negative integer.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.

    Examples:
        factorial(5) -> 120
        factorial(0) -> 1
    """
    raise NotImplementedError("Implement factorial function")


if __name__ == "__main__":
    print("BreakItTillYouMakeIt functions loaded. Run your tests to verify.")
