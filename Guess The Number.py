# Darlene Lopez
# Guess The Number
# A script that plays “guess the number.” Choose the number to be guessed by selecting a random integer in the range 1 to 1000

import random

# Function to get an integer from user input
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main game function
def play_game():
    # Generate a random number between 1 and 1000
    number_to_guess = random.randint(1, 1000)
    guess_count = 0
    print("Guess my number between 1 and 1000 with the fewest guesses:")

    while True:
        # Get the player's guess
        guess = get_int_input("Enter your guess: ")
        guess_count += 1

        # Check the guess
        if guess < number_to_guess:
            print("Too low. Try again.")
        elif guess > number_to_guess:
            print("Too high. Try again.")
        else:
            print("Congratulations. You guessed the number!")
            break

    # Display feedback based on the number of guesses
    if guess_count <= 10:
        print("Either you know the secret or you got lucky!")
    else:
        print("You should be able to do better!")

    # Ask the player if they want to play again
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()  # Start a new game
    else:
        print("Thanks for playing! Goodbye.")

play_game()
