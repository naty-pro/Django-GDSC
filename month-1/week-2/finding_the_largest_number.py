# Function to find the largest number in a list
def find_largest(numbers):
    if not numbers:
        return None  # Handle empty list case
    return max(numbers)

# Example 
numbers_list = [10, 5, 12, 33, 8, 20, 3]

# Largest number
print("Largest number:", find_largest(numbers_list))
