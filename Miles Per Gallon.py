# Initialize total miles and gallons
total_miles = 0
total_gallons = 0

# Function to get a float from user input
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Loop to take user input until the sentinel value (-1) is entered
while True:
    # Prompt the user to enter gallons used, and check for sentinel value
    gallons_used = get_float_input("Enter the gallons used (-1 to end): ")
    if gallons_used == -1:
        break  # Exit the loop if the user enters -1

    # Prompt the user to enter miles driven
    miles_driven = get_float_input("Enter the miles driven: ")

    # Calculate miles per gallon for the current tank
    mpg = miles_driven / gallons_used
    print(f"The miles/gallon for this tank was {mpg:.6f}")

    # Add to total miles and gallons
    total_miles += miles_driven
    total_gallons += gallons_used

# After the loop ends, calculate and display the overall average MPG
if total_gallons != 0:
    overall_mpg = total_miles / total_gallons
    print(f"The overall average miles/gallon was {overall_mpg:.6f}")
else:
    print("No valid data entered, so no average MPG can be calculated.")
