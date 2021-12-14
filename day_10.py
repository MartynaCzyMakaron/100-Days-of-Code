def print_operations(array):
    for i in array:
        print(i)


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        raise ValueError("You can't divide by 0!!!")
    else:
        return first / second

def calculator():
    continues = True
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    first_number = float(input("Enter your first number "))
    prev_result = first_number
    while continues:
        print_operations(operations)
        operation = input("Pick an operation ")
        second_number = float(input("Enter your second number "))
        calculation_function = operations[operation]
        result = calculation_function(prev_result, second_number)
        print(f"{prev_result} " + operation + f" {second_number} = " + str(result))
        prev_result = result

        decision = input("press 'y' if you want to continue or 'n' to restart calculator")
        if decision == 'n':
            continues = False
            calculator()

calculator()
