"""
BreakItTillYouMakeIt - Text & Math Utility Functions
Author: Kabelo Bongani Maile
Instructions: Implement each function below according to the docstrings.
Then write unit tests to verify correctness.
"""

def count_words(text: str) -> dict:
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
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        row = [1] 
        for k in range(1, n + 1):
            # Calculate next coefficient using the previous one
            coeff = row[k - 1] * (n - k + 1) // k
            row.append(coeff)
        
    return row  # Return the completed row


def calculator(a: float, b: float, op: str) -> float:
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
    words = text.split()
    words.reverse()
    text = " ".join(words)
    return text


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i

    return result


if __name__ == "__main__":
    print("BreakItTillYouMakeIt functions loaded. Run your tests to verify.")
