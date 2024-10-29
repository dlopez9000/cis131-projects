# Darlene Lopez
# CIS 131
# This program uses a recursive function power(base, exponent) that than returns

# Recursive function to calculate base^exponent
def power(base, exponent):
    # Terminating condition: if exponent is 1, return base
    if exponent == 1:
        return base
    # Recursive step: multiply base by the result of power(base, exponent - 1)
    else:
        return base * power(base, exponent - 1)

# Program to take input and call the power function
try:
    base = float(input("Enter the base: "))
    exponent = int(input("Enter the exponent (positive integer): "))
    if exponent < 1:
        print("Exponent should be a positive integer greater than or equal to 1.")
    else:
        result = power(base, exponent)
        print(f"{base}^{exponent} = {result}")
except ValueError:
    print("Please enter valid numbers for base and exponent.")
    # Main loop for continuous input
    while True:
        try:
            base = float(input("Enter the base (or type 'exit' to quit): "))
            exponent = int(input("Enter the exponent (positive integer): "))

            if exponent < 1:
                print("Exponent should be a positive integer greater than or equal to 1.")
                continue

            result = power(base, exponent)
            print(f"{base}^{exponent} = {result}")

        except ValueError:
            # Check if the user typed 'exit' to quit
            exit_input = input(
                "If you want to exit, type 'exit'. Otherwise, please enter valid numbers for base and exponent.")
            if exit_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break
