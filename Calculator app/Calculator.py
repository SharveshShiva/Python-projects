import art
def calculator():
    print(art.logo)

    first_number = float(input("What's your first number?: "))
    should_continue = True

    while should_continue:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        next_number = float(input("What is the next number?: "))

        def add(a, b):
            """This function adds 2 numbers."""
            return a + b

        def sub(a, b):
            """This function subtracts 2 numbers."""
            return a - b

        def mul(a, b):
            """This function multiplies 2 numbers."""
            return a * b

        def div(a, b):
            """This function divides 2 numbers."""
            return a / b

        operation_dictionary = {
            "+": add(first_number, next_number), "-": sub(first_number, next_number),
            "*": mul(first_number, next_number), "/": div(first_number, next_number),
        }

        addition = operation_dictionary["+"]
        subtraction = operation_dictionary["-"]
        multiplication = operation_dictionary["*"]
        division = operation_dictionary["/"]

        n = 0

        if operation == "+":
            print(f"{first_number} + {next_number} = {addition}")
            n = addition
        elif operation == "-":
            print(f"{first_number} - {next_number} = {subtraction}")
            n = subtraction
        elif operation == "*":
            print(f"{first_number} * {next_number} = {multiplication}")
            n = multiplication
        else:
            print(f"{first_number} / {next_number} = {division}")
            n = division
        operation_again = input(f"Type 'y' to continue calculating with {n} or type 'n' to start a new calculation: ")

        if operation_again == 'y':
            first_number = n

        elif operation_again == 'n':
            should_continue = False
            print("\n"*100)
            calculator()
        else:
            exit()

calculator()

