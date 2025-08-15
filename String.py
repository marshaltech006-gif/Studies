# Single-line comment example
letter = 'p'  # a single character
print(letter)           # p
print(len(letter))      # 1

# Strings can be in single or double quotes
greeting = "Hello, World!"
print(greeting)         # Hello, World!
print(len(greeting))    # 13

# Multi-line strings
multi_line = '''I am learning Python
and enjoying the process.
One day, I'll be a pro gamer and coder.'''
print(multi_line)

# Another way
multi_line_2 = """This is also 
a multi-line string."""
print(multi_line_2)

# String concatenation
first_name = 'Marshal'
last_name = 'Tech'
full_name = first_name + " " + last_name
print(full_name)        # Marshal Tech
print(len(first_name))  # 7
print(len(last_name))   # 4

# Unpacking string
language = 'Python'
a, b, c, d, e, f = language
print(a, b, c, d, e, f)

# Indexing
print(language[0])      # P
print(language[-1])     # n

# Slicing
print(language[0:3])    # Pyt
print(language[-3:])    # hon
print(language[::2])    # Pto

# Reverse string
print(language[::-1])   # nohtyP

# Escape sequences
print("Line 1\nLine 2")  # new line
print("Tab\tSpace")      # tab
print("This is a backslash: \\")
print('Single quote: \'')
print("Double quote: \"")

# String methods
name = "marshal tech"
print(name.capitalize())  # Marshal tech
print(name.title())       # Marshal Tech
print(name.upper())       # MARSHAL TECH
print(name.lower())       # marshal tech
print(name.swapcase())    # MARSHAL TECH -> mARSHAL TECH

# Count
challenge = 'thirty days of python'
print(challenge.count('t'))      # 3
print(challenge.count('th'))     # 2
print(challenge.count('y', 7, 14))  # 1

# Endswith
print(challenge.endswith('python'))  # True

# Find
print(challenge.find('days'))    # 7
print(challenge.find('x'))       # -1

# Format
age = 20
city = "Mahabubabad"
print("I am {} from {}.".format(first_name, city))

# f-string (cleaner)
print(f"I am {first_name} from {city}, age {age}.")

# Join
words = ["Python", "is", "fun"]
print(" ".join(words))   # Python is fun

# Strip
text = "   Hello   "
print(text.strip())      # Hello

# Replace
print("I love Java".replace("Java", "Python"))

# Split
print(challenge.split())     # ['thirty', 'days', 'of', 'python']

# Startswith
print(challenge.startswith('thirty'))  # True