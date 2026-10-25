
# 1. append() - Adds an item at the end
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)  # Output: [10, 20, 30, 40]


# 2. extend() - Adds multiple items
numbers = [10, 20]
numbers.extend([30, 40])
print(numbers)  # Output: [10, 20, 30, 40]


# 3. insert() - Inserts an item at a given index
numbers = [10, 30, 40]
numbers.insert(1, 20)
print(numbers)  # Output: [10, 20, 30, 40]


# 4. remove() - Removes the first matching value
numbers = [10, 20, 30, 20]
numbers.remove(20)
print(numbers)  # Output: [10, 30, 20]


# 5. pop() - Removes and returns an item
numbers = [10, 20, 30]
removed = numbers.pop()
print(numbers)  # Output: [10, 20]
print(removed)  # Output: 30

# Remove using an index
numbers.pop(0)
print(numbers)  # Output: [20]


# 6. clear() - Removes all items
numbers = [10, 20, 30]
numbers.clear()
print(numbers)  # Output: []


# 7. index() - Returns the index of an item
fruits = ["apple", "banana", "mango"]
print(fruits.index("banana"))  # Output: 1


# 8. count() - Counts occurrences
numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))  # Output: 3


# 9. sort() - Sorts in ascending order
numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)  # Output: [10, 20, 30, 40]

# Sort in descending order
numbers.sort(reverse=True)
print(numbers)  # Output: [40, 30, 20, 10]


# 10. reverse() - Reverses the list in place
numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)  # Output: [40, 30, 20, 10]


# 11. copy() - Creates a shallow copy
original = [10, 20, 30]
new_list = original.copy()
new_list.append(40)

print(original)  # Output: [10, 20, 30]
print(new_list)  # Output: [10, 20, 30, 40]
