### Calculator
from art import logo


#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def mult(n1, n2):
    return n1 * n2


#Divide
def div(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": mult, "/": div}
trigger = "y"


def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    for keys in operations:
        print(keys)

    while trigger == "y":
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        ) == "y":
            num1 = answer
        else:
            trigger == "n"
            calculator()


calculator()
