# Darlene Lopez
# CIS 131
# This program calculates a class-average script in which you could enter any number of grades.

def write_grades_to_file(filename="grades.txt"):
    with open(filename, 'w') as file:
        while True:
            try:
                # Ask for a grade input from the user
                grade_input = input("Enter a grade (or -1 to finish): ").strip()

                # Check if the input is numeric
                if not grade_input.replace('.', '', 1).isdigit() and grade_input != '-1':
                    raise ValueError("Non-numeric input received.")

                # Convert input to float
                grade = float(grade_input)

                # Exit condition: if grade is -1, stop the input loop
                if grade == -1:
                    break

                # Check for valid grade range
                if grade < 0 or grade > 100:
                    print("Grade must be between 0 and 100.")
                    continue

                # Write the valid grade to the file
                file.write(f"{grade}\n")

            except ValueError as e:
                # Handle invalid inputs and show an error message
                print(f"Invalid input: {e}. Please enter a valid numeric grade or -1 to finish.")

    print(f"Grades have been saved to {filename}.")

# Run the function
write_grades_to_file()
