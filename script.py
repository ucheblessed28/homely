# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))
# operation = input("Enter the operation (+, -, *, /): ")
# result = None
# if operation == "+":
#     result = a + b
# elif operation == "-":
#     result = a - b
# elif operation == "*":
#     result = a * b
# elif operation == "/":
#     if b != 0:
#         result = a / b
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Error: Invalid operation.")
# if result is not None:
#     print(f"The result of {a} {operation} {b} is: {result}")
# This code is a simple calculator that takes two numbers and an operation as input from the user.
# It performs the specified operation and prints the result.
# The calculator supports addition, subtraction, multiplication, and division.
# It also handles division by zero and invalid operations gracefully.
# The code is written in Python and can be run in any Python environment.
# The calculator is a basic example of how to use conditional statements and user input in Python.
# The code can be further improved by adding more operations, error handling, and user interface enhancements.
# The calculator can be used as a command-line tool or integrated into a larger application.
# The calculator can be extended to support more complex operations, such as exponentiation, square roots, and trigonometric functions.
# The calculator can also be modified to support multiple operations in a single expression, such as "2 + 3 * 4".
# The calculator can be further improved by adding a graphical user interface (GUI) using libraries like Tkinter or PyQt.
# The calculator can be used as a learning tool for beginners to understand basic programming concepts in Python.

import math
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
# The result of the Pythagorean theorem is printed
print(f"The result of the Pythagorean theorem with sides {a} and {b} is: {c}")