# Darlene Lopez
# Target Heart Rate Calculator
# This program calculates the safe estimate for heart rate during exercise 

while True:
    # Input age
    age_input = input("Please enter your age (or type 'x' to exit): ")

    if age_input.lower() == "x":
        print("Exiting the program.")
        break
    
    if not age_input.isdigit():
        print("Error: Please enter a valid number.")
        continue

    # Convert the input to an integer
    age = int(age_input)

    # Calculate maximum heart rate
    max_heart_rate = 220 - age

    # Calculate target heart rate range (50% to 85% of maximum heart rate)
    target_heart_rate_min = 0.50 * max_heart_rate
    target_heart_rate_max = 0.85 * max_heart_rate

    # Display the results
    print(f"Maximum Heart Rate: {max_heart_rate} beats per minute")
    print(f"Target Heart Rate Range: {target_heart_rate_min:.1f} to {target_heart_rate_max:.1f} beats per minute")
    print("-" * 50)
