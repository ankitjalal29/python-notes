
# Python Tuple Methods and Operations

t = (10, 20, 30, 20, 40)

# 1. count() - Counts occurrences of an element
print(t.count(20))       # Output: 2

# 2. index() - Returns the first index of an element
print(t.index(30))       # Output: 2
print(t.index(20))       # Output: 1

# 3. len() - Returns the length of tuple
print(len(t))            # Output: 5

# 4. max() - Returns the maximum value
print(max(t))            # Output: 40

# 5. min() - Returns the minimum value
print(min(t))            # Output: 10

# 6. sum() - Returns the sum of elements
print(sum(t))            # Output: 120

# 7. sorted() - Returns a sorted list
print(sorted(t))         # Output: [10, 20, 20, 30, 40]

# 8. Membership operators
print(20 in t)           # Output: True
print(50 not in t)       # Output: True

# 9. Indexing
print(t[0])              # Output: 10
print(t[-1])             # Output: 40

# 10. Slicing
print(t[1:4])            # Output: (20, 30, 20)
print(t[:3])             # Output: (10, 20, 30)
print(t[2:])             # Output: (30, 20, 40)

# 11. Concatenation - Joins two tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)           # Output: (1, 2, 3, 4, 5, 6)

# 12. Repetition - Repeats tuple elements
print(t1 * 2)            # Output: (1, 2, 3, 1, 2, 3)

# 13. Tuple packing
packed = 10, 20, 30
print(packed)            # Output: (10, 20, 30)

# 14. Tuple unpacking
a, b, c = packed
print(a)                 # Output: 10
print(b)                 # Output: 20
print(c)                 # Output: 30

# 15. Single-element tuple
single = (10,)
print(type(single))      # Output: <class 'tuple'>

# 16. Convert list into tuple
my_list = [1, 2, 3]
print(tuple(my_list))    # Output: (1, 2, 3)

# 17. Convert tuple into list
print(list(t1))          # Output: [1, 2, 3]

# 18. Check tuple type
print(type(t))           # Output: <class 'tuple'>

# 19. Nested tuple
nested = ((1, 2), (3, 4))
print(nested[0])         # Output: (1, 2)
print(nested[1][0])      # Output: 3

# 20. Loop through tuple
for item in t1:
    print(item)          # Output: 1, then 2, then 3 (each on a new line)
