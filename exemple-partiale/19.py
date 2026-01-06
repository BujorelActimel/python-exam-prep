size_BN = 0

while True:
    command = input(">>> ")
    if command == "A":
        size_BN = float(input("Set the size:\n"))

    elif command == "S":
        square_area_BN = size_BN * size_BN
        print(f"The area of a square having a side of {size_BN} is {square_area_BN}")

    elif command == "Q":
        break

    else:
        print("Please insert a valid menu option")
