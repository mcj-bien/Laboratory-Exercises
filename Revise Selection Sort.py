def sort_numbers(numbers):
    # Using Python's built-in sort
    return sorted(numbers)

def main():
    # Read 10 numbers from input
    numbers = list(map(int, input("Enter 10 numbers separated by space: ").split()))
    
    if len(numbers) != 10:
        print("Please enter exactly 10 numbers.")
        return
    
    # Sort the numbers
    sorted_numbers = sort_numbers(numbers)
    
    # Display results
    print("Sorted numbers:", sorted_numbers)

if __name__ == "__main__":
    main()