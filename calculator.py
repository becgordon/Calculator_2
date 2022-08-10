"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    equation = input("Equation? ")
    tokens = equation.split(" ")
    operand = tokens[0]
    result = ""

    if "q" in tokens:
        print("Bye!")
        break

    num1 = tokens[1]

    if len(tokens) > 2:
        num2 = tokens[2]

    if operand == "+":
        result = add(float(num1),float(num2))
    
    elif operand == "-":
        result = subtract(float(num1),float(num2))
    
    elif operand == "*":
        result = multiply(float(num1),float(num2))
    
    elif operand == "/":
        result = divide(float(num1),float(num2))
    
    elif operand == "square":
        result = square(float(num1))

    elif operand == "cube":
        result = cube(float(num1))
    
    elif operand == "pow":
        result = power(float(num1),float(num2))
    
    elif operand == "mod":
        result = mod(float(num1),float(num2))
    print(result)

