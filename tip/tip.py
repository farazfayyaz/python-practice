def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Takes string
    # Removes "$" and converts to float int
    return float(d[1:])


def percent_to_float(p):
    # Takes string
    # Remove "%", converts whole number into float percentage form
    return float(int(p[:2]) / 100) 


main()