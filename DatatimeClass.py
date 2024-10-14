# Darlene Lopez
# CIS 131
# This program contains a datetime class for manipulating dates and times and is view only.

from datetime import datetime

x = datetime.now()  # Capture current time

y = datetime.now()  # Capture current time again

# Display each datetime object
print(f"x: {x}")
print(f"y: {y}")

# Display each datetime object's data attributes individually
print(f"x attributes - Year: {x.year}, Month: {x.month}, Day: {x.day}, "
      f"Hour: {x.hour}, Minute: {x.minute}, Second: {x.second}, Microsecond: {x.microsecond}")
print(f"y attributes - Year: {y.year}, Month: {y.month}, Day: {y.day}, "
      f"Hour: {y.hour}, Minute: {y.minute}, Second: {y.second}, Microsecond: {y.microsecond}")

# Use the comparison operators to compare the two datetime objects
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")

# Calculate the difference between y and x
difference = y - x
print(f"Difference between y and x: {difference}")
