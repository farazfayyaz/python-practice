def formula(mass):
    return mass * 300000000 ** 2

def main():
    user_mass = int(input("m: "))
    print("E: " + str(formula(user_mass)))


main()