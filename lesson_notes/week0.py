# Pseudocode - comments to write code in plain english

# name = variable
# input(...) = stores user response
name = input("What's your name? ")

# .strip() = method to remove empty spaces before and after user input
name = name.strip() 

# print(...) = displays in terminal
print("Hello", name)

name2 = input("What's your name? ").strip().title() # methods can be put on a single line
print(f"Hello {name}") # template literal - similar to JavaScript

# int = datatype for integers/whole numbers

# +,-,*,/,% = math symbols
# Concatenation = strings are added together
# REMINDER: When adding numbers, make sure they are converted to int/float
# Numbers must be str when in sentence

x = 5
y = 4
z = x + y
print(z)

a = input("What's a? ")
b = input("What's b? ")
c = int(a) + int(b)
print(c)

# float = datatype for decimal numbers

f = float(input("What's f? "))
d = float(input("What's d? "))

# round(number [, n-digits])
z = round(f + d) # EX: 4.6 -> 5
# round(f + d, 2) EX: 0.6666666 -> 0.67
print(z)

# print(f"{z:,}")  :, - setting format to commas for longer numbers
# 1000 -> 1,000

# print(f"{z:.2f}")   .2f - another way to round up to 2 decimal places

# def = start a function

def hello(): # a function named hello
    print("Hello")

hello() # must call a function to use it

def hello_name(name): # a function with 1 paramater
    print("Hello", name)

hello_name(name)