def convert(str):
    return str.replace(":)","🙂").replace(":(", "🙁")

def main():
    userInput = input("Enter phrase: ")
    print(convert(userInput))

main()