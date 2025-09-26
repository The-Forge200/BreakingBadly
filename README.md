# BreakingBadly
**NB!!** -- Create a branch first.
```bash
git checkout -b <branch-name>
git push -u origin <branch-name>
```

## 📝 Purpose

Welcome to BreakingBadly! This exercise is designed to help you practice Test-Driven Development (TDD) and strengthen your unit testing skills.
The main goal is not just to implement functions, but to think critically about how to test your code. You’ll learn how to write clear, meaningful tests and verify your implementations, which is a core skill for any software engineer.

## 📚 Exercise Overview

You have a single Python file in this repo. It is completely empty. Your task is to:

* Implement the functions yourself according to the instructions provided in the docstrings.
* Write your own unit tests using Python’s built-in **unittest** library.

The functions you’ll be implementing include:

* count_words(text: str) -> dict
* pascals_triangle_row(n: int) -> list[int]
* calculator(a: float, b: float, op: str) -> float
* reverse_words(text: str) -> str
* factorial(n: int) -> int

## 🛠 Instructions
Open the Python file provided (tobuild.py).
Read the docstrings for each function carefully. They describe:
   * What the function should do
   * Arguments it receives
   * Expected return values

### Examples to guide your implementation
Implement each function from scratch.
The unittest file is already created for you under tests/tobreak.py
Run your tests frequently to check your code. Use:
python -m unittest test_utils.py
You can also use the beaker on VSCode to run your code.

Make sure your tests cover different cases, including edge cases (like empty strings, zero, division by zero, etc.).

🎯 Learning Goals

This exercise is mainly focused on your testing practices, not just on getting the correct results. By completing this exercise, you will:
Learn how to write unit tests from scratch.
Practice thinking in terms of TDD: writing tests first, thinking about edge cases, and verifying outputs.
Improve your ability to structure and organize code in a testable way.


✅ Success Criteria
All functions are implemented correctly.
Unit tests are written for each function, covering normal and edge cases.
Tests run without errors and demonstrate a clear understanding of testing practices.
