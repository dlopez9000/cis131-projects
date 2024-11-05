# Darlene Lopez
# CIS 131
# Tower of Hanoi program

def hanoi(n, source, target, auxiliary):
    # Check if the number of disks is a valid positive integer
    if n <= 0:
        print("Error: Number of disks must be a positive integer.")
        return

    if n == 1:
        print(f"{source} → {target}")
        return
    # Move n-1 disks from source to auxiliary, using target as a temporary peg
    hanoi(n - 1, source, auxiliary, target)
    # Move the nth disk from source to target
    print(f"{source} → {target}")
    # Move the n-1 disks from auxiliary to target, using source as a temporary peg
    hanoi(n - 1, auxiliary, target, source)


# Define the number of disks for practical testing
num_disks = 5  # Use a smaller number like 3 for testing; change to 64 for the full problem
# Call the function with peg numbers as 1, 3, and 2
hanoi(num_disks, 1, 3, 2)
