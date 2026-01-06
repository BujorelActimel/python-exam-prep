size_BN = 0
pi = 3.14

while True:
    command = input(">>> ")
    if command == "A":
        size_BN = float(input("Set the size:\n"))

    elif command == "C":
        cicle_area_BN = pi * size_BN * size_BN
        print(f"The area of a circle having a radius of {size_BN} is {cicle_area_BN}")

    elif command == "Q":
        break

    else:
        print("Please insert a valid menu option")