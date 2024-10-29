# Darlene Lopez
# CIS 131
# This program has been modified to fix the recursive fibonacci function.

# Initialize a counter for tracking function calls
call_count = 0

def fibonacci(n):
    global call_count
    call_count += 1  # Increment the counter each time fibonacci is called
    if n in (0, 1):  # Base cases
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Function to reset and calculate fibonacci along with call count
def fibonacci_with_call_count(n):
    global call_count
    call_count = 0  # Reset the counter
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result}, Total function calls: {call_count}")

# Display the number of calls for fibonacci(10), fibonacci(20), and fibonacci(30)
fibonacci_with_call_count(10)
fibonacci_with_call_count(20)
fibonacci_with_call_count(30)
