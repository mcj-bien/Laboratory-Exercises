# Program to analyze scores

# Read input scores from one line, separated by spaces
scores = list(map(float, input("Enter the numbers: ").split()))

# Calculate average
average = sum(scores) / len(scores)

# Count scores above or equal to average, and below average
above_or_equal = sum(1 for s in scores if s >= average)
below = sum(1 for s in scores if s < average)

# Display results
print(f"Average is {average}")
print(f"Number of scores above or equal to the average: {above_or_equal}")
print(f"Number of scores below the average: {below}")
