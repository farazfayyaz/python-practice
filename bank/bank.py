# if "Hello" = output $0
# if "H" and not "Hello"= output $20
# if anything else = output $100

def greet_check(str):
    if (str[0:5].lower() == "hello"):
        print("$0")
    elif str[0].lower() == "h" and str[0:5].lower() != "hello":
        print("$20")
    else:
        print("$100")

greet_check("Hello")
greet_check("Hello, Faraz")
greet_check("How you doing?")
greet_check("What's happening?")