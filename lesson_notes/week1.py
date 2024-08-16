# conditionals = check if a statement is True
# >, >=, <, <=, ==, !=
# if statements = check a statement and produces a result based on statement

x = int(input("What's x? "))
y = int(input("What's y? "))

# if = check first conditional
# elif = check another conditional
# else = default result

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# or = if 1 statement is true, return true - both false = false
# and = both statements are true, return true - else false

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# != (not equal) = "not true"

name = input("What's your name? ")

# match = switch case, alternative to if else statements

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # base case, anything that isn't in the match list
        print("Who?")
