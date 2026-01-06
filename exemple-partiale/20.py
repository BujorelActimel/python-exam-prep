size_BN = 0

while True:
    command = input(">>> ")
    if command == "A":
        size_BN = float(input("Set the size:\n"))

    elif command == "P":
        square_perimeter_BN = 4 * size_BN
        print(f"The perimeter of a square having a side of {size_BN} is {square_perimeter_BN}")

    elif command == "Q":
        break

    else:
        print("Please insert a valid menu option")
