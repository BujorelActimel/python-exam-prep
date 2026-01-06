size_BN = 0
pi = 3.14

while True:
    command = input(">>> ")
    if command == "A":
        size_BN = float(input("Set the size:\n"))

    elif command == "D":
        circle_perimeter_BN = 2 * pi * size_BN
        print(f"The perimeter of a circle having a radius of {size_BN} is {circle_perimeter_BN}")

    elif command == "Q":
        break

    else:
        print("Please insert a valid menu option")