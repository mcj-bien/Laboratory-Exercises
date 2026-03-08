def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        # After each pass, the largest element is at the end
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                # Swap
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def main():
    # Read 10 numbers
    numbers = list(map(int, input("Enter 10 numbers separated by space: ").split()))
    
    if len(numbers) != 10:
        print("Please enter exactly 10 numbers.")
        return
    
    sorted_numbers = bubble_sort(numbers)
    print("Sorted numbers:", sorted_numbers)

if __name__ == "__main__":
    main()
