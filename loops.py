# printezi pe ecran toate numerele de la 1 la 100

# conditie = 2 == 2

# if conditie:
#     print("if")

# x = 2
# while x <= 100:
#     print(x)
#     x = x + 2

# for x in range(1, 101):
#     print(x)


numar = int(input("introduceti un numar: "))

# afisez suma cifrelor

# 123 -> 6
# 333 -> 9

suma = 0

# chestii
while numar > 0:
    ultimaCifra = numar % 10
    suma = suma + ultimaCifra
    numar = numar // 10

print(suma)
