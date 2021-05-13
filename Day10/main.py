from art import logo


# Calculator
# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Print logo and define operators dictionary
operator_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# calculator function
def calculator():
    print(logo)
    keep_going = True  # loop controler
    n1 = float(input("Type the first number: "))
    print("\nOperator Selection\n")

    while keep_going:
        for key in operator_dictionary:
            print(key)

        operator = input("\nPlease, select one operator from the lines above: ")
        n2 = float(input("Type the next number: "))
        function = operator_dictionary[operator]
        answer = function(n1, n2)
        print(f"{n1} {operator} {n2} = {answer}\n")
        # control input for new round of calculation or closing program
        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to begin new calculation: \n").lower() == "y":
            # to keep answer in variable n1 and keep operating with this last value
            n1 = answer
        else:
            keep_going = False
            calculator()


# Start
calculator()
