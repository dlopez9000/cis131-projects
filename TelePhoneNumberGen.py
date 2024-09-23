# Darlene Lopez
# CIS131
# This program generates every possible seven-letter word combination corresponding to a 7-digit number

from itertools import product

# Dictionary mapping digits to letters
digit_to_letters = {
    '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
    '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'
}


def generate_combinations(phone_number):
    # Create a list of corresponding letter groups for each digit in the phone number
    letters = [digit_to_letters[digit] for digit in phone_number]

    # Generate all possible combinations
    combinations = [''.join(combo) for combo in product(*letters)]

    return combinations


def sanitize_input(phone_number):
    # Remove any non-digit characters and check for invalid digits (0 or 1)
    sanitized = ''.join([char for char in phone_number if char.isdigit()])

    # Ensure length is exactly 7 and no digits are 0 or 1
    if len(sanitized) != 7 or any(digit in '01' for digit in sanitized):
        return None
    return sanitized


def main():
    while True:
        # Prompt user for input
        user_input = input("\nEnter a 7-digit phone number (without 0 or 1), or type 'exit' to quit: ").strip()

        # Exit condition
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Sanitize the input
        phone_number = sanitize_input(user_input)

        if phone_number is None:
            print("Invalid input. Please ensure it's a 7-digit number without 0 or 1.")
        else:
            # Generate and display combinations
            combinations = generate_combinations(phone_number)
            print(f"Total combinations: {len(combinations)}")
            print("Sample combinations:")
            print(combinations[:37])  # Print the first 37 combinations for brevity


# Run the program
main()
