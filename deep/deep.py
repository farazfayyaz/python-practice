user_input = input("Please enter the answer to the Great Question of Life, the Universe and Everything: ")

# strip() = clears the empty space before and after the input
# lower() = changes input into lower letters
user_input_fixed = user_input.strip().lower()

# 3 possible answers: number, dash, no dash
answer1 = "42"
answer2 = "forty-two"
answer3 = "forty two"

if(user_input_fixed == answer1 or user_input_fixed == answer2 or user_input_fixed == answer3):
    print("Yes")
else:
    print("No")