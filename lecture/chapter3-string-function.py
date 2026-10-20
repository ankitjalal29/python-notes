
text = "  Hello Python World  "
name = "ankit jalal"
sentence = "Python is easy to learn"
word = "Python"

# 1. upper() - Converts to uppercase
print(text.upper())                 # Output: "  HELLO PYTHON WORLD  "

# 2. lower() - Converts to lowercase
print(text.lower())                 # Output: "  hello python world  "

# 3. capitalize() - First character uppercase
print(name.capitalize())            # Output: Ankit jalal

# 4. title() - First letter of each word uppercase
print(name.title())                 # Output: Ankit Jalal

# 5. swapcase() - Changes uppercase to lowercase and vice versa
print("Hello Python".swapcase())    # Output: hELLO pYTHON


# 6. strip() - Removes spaces from both ends
print(text.strip())                 # Output: Hello Python World

# 7. lstrip() - Removes spaces from the left
print(text.lstrip())                # Output: Hello Python World  

# 8. rstrip() - Removes spaces from the right
print(text.rstrip())                # Output:   Hello Python World


# 9. find() - Finds the position of a substring
print(sentence.find("easy"))        # Output: 11

# 10. index() - Returns the position of a substring
print(sentence.index("easy"))       # Output: 11

# 11. count() - Counts occurrences
print("banana".count("a"))          # Output: 3

# 12. startswith() - Checks the beginning
print(sentence.startswith("Python")) # Output: True

# 13. endswith() - Checks the ending
print(sentence.endswith("learn"))   # Output: True


# 14. replace() - Replaces old text with new text
print(sentence.replace("easy", "fun")) 
# Output: Python is fun to learn


# 15. split() - Converts a string into a list
print(sentence.split())             # Output: ['Python', 'is', 'easy', 'to', 'learn']

# 16. join() - Joins strings using a separator
print("-".join(["Python", "is", "easy"])) 
# Output: Python-is-easy

# 17. splitlines() - Splits text at line breaks
print("Hello\nPython\nWorld".splitlines())
# Output: ['Hello', 'Python', 'World']


# 18. isalpha() - Checks whether all characters are letters
print("Python".isalpha())           # Output: True

# 19. isdigit() - Checks whether all characters are digits
print("12345".isdigit())             # Output: True

# 20. isalnum() - Checks letters and digits only
print("Python123".isalnum())         # Output: True

# 21. islower() - Checks lowercase letters
print("hello".islower())             # Output: True

# 22. isupper() - Checks uppercase letters
print("HELLO".isupper())             # Output: True

# 23. isspace() - Checks whitespace only
print("   ".isspace())               # Output: True

# 24. istitle() - Checks title case
print("Hello World".istitle())       # Output: True


# 25. len() - Returns the number of characters
print(len(word))                     # Output: 6

# 26. Indexing - Accesses individual characters
print(word[0])                       # Output: P
print(word[-1])                      # Output: n

# 27. Slicing - Extracts part of a string
print(word[0:3])                     # Output: Pyt

# 28. Reverse slicing - Reverses the string
print(word[::-1])                    # Output: nohtyP


# 29. in - Checks whether text exists
print("Python" in sentence)          # Output: True

# 30. not in - Checks whether text does not exist
print("Java" not in sentence)        # Output: True


# 31. f-string - Inserts variables into a string
age = 20
print(f"My name is {name} and I am {age} years old.")
# Output: My name is ankit jalal and I am 20 years old.

# 32. format() - Inserts values into placeholders
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is ankit jalal and I am 20 years old.


# 33. center() - Centers text with padding
print("Python".center(20, "*"))      # Output: *******Python*******

# 34. ljust() - Left-aligns the string
print("Python".ljust(10, "-"))       # Output: Python----

# 35. rjust() - Right-aligns the string
print("Python".rjust(10, "-"))       # Output: ----Python

# 36. zfill() - Adds zeros at the beginning
print("42".zfill(5))                 # Output: 00042


# 37. partition() - Splits into three parts
print(sentence.partition("is"))
# Output: ('Python ', 'is', ' easy to learn')


# 38. encode() - Converts a string into bytes
print("Python".encode())             # Output: b'Python'


# 39. removeprefix() - Removes a prefix if present
print("Python Programming".removeprefix("Python "))
# Output: Programming

# 40. removesuffix() - Removes a suffix if present
print("notes.txt".removesuffix(".txt"))
# Output: notes

