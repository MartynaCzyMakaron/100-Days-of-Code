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


continues = True
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

while continues:
    first_number = int(input("Enter your first number "))
    print_operations(operations)
    operation = input("Pick an operation ")
    second_number = int(input("Enter your second number "))
    calculation_function = operations[operation]
    result = calculation_function(first_number, second_number)
    print(f"{first_number} " + operation + f" {second_number} = " + str(result))

    decision = input("press 'y' if you want to continue ")
    if decision != 'y':
        continues = False
