# Darlene Lopez
# 7% investemnt assignment
# This program calculates years 10, 20, and 30 automatically but user is able to input more years to calculate

def calculate_investment(principal, rate, years):
    amount = principal * (1 + rate) ** years
    return amount

# Parameters
principal = 1000  # initial investment
annual_rate_of_return = 0.07  # 7% annual return

# Calculate for 10, 20, and 30 years
amount_10_years = calculate_investment(principal, annual_rate_of_return, 10)
amount_20_years = calculate_investment(principal, annual_rate_of_return, 20)
amount_30_years = calculate_investment(principal, annual_rate_of_return, 30)

print(f"Amount after 10 years: ${amount_10_years:.2f}")
print(f"Amount after 20 years: ${amount_20_years:.2f}")
print(f"Amount after 30 years: ${amount_30_years:.2f}")

# Loop for user input and to calculate other years
while True:
    user_input = input("Enter the number of years you want to calculate the investment for (or type 'x' to exit): ").strip()
    if user_input.lower() == 'x':
        print("Exiting the program.")
        break
    try:
        user_years = int(user_input)
        user_amount = calculate_investment(principal, annual_rate_of_return, user_years)
        print(f"Amount after {user_years} years: ${user_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number of years or 'x' to exit.")
