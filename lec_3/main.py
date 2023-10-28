def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero!"
    return a / b

while True:
    print("Enter 'add' for addition")
    print("Enter 'sub' for subtraction")
    print("Enter 'mul' for multiplication")
    print("Enter 'div' for division")

    operation = input("Operation:    ")

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if operation == "add":
        print(f"{number1} + {number2} = ", add(number1, number2))
    elif operation == "sub":
        print(f"{number1} - {number2} = ", subtract(number1, number2))
    elif operation == "mul":
        print(f"{number1} * {number2} = ", multiply(number1, number2))
    elif operation == "div":
        print(f"{number1} / {number2} = ", divide(number1, number2))
    else:
        print("Invalid input, try again!")
    continue_calculations = input("Continue calculate? [yes/no]:    ")
    if(continue_calculations == "no"):
        break

