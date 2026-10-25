
numbers = [10, 20, 30, 40, 50]

print(len(numbers))       # Output: 5
print(max(numbers))       # Output: 50
print(min(numbers))       # Output: 10
print(sum(numbers))       # Output: 150
print(sorted(numbers))    # Output: [10, 20, 30, 40, 50]

# Check whether an item exists
print(30 in numbers)      # Output: True
print(100 in numbers)     # Output: False

# Access items using indexing
print(numbers[0])         # Output: 10
print(numbers[-1])        # Output: 50

# Slicing
print(numbers[1:4])       # Output: [20, 30, 40]
print(numbers[::-1])      # Output: [50, 40, 30, 20, 10]
