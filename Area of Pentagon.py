import math

# Prompt the user for the side length
s = float(input("Enter the side: "))

# Compute the area using the formula
area = (5 * s**2) / (4 * math.tan(math.pi / 5))

# Display the result
print("The area of the pentagon is", area)