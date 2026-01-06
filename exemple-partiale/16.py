Carla_BN = input("Did Simona defeat Carla?\n") # 1
Serena_BN = input("Did Simona defeat Serena?\n") # 1 
Camilla_BN = input("Did Serena defeat Camilla?\n")

if (Carla_BN == "1" and Serena_BN == "1") or (Serena_BN == "0" and Camilla_BN == "0"):
    print("It is True that Simona remains number 1")
else:
    print("It is False that Simona remains number 1")
