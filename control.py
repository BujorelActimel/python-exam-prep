# Structura:

# conditie = 10 == 20

# if conditie:
#     print("a")
# else:
#     print("b")


varsta = int(input("Ce varsta aveti? "))

# caz 1 - sub 14 - nu trebuie sa iti faci
# caz 2 - fix 14 ani - trebuie sa iti faci
# caz 3 - de la 15 la 17 - nu trebuie sa iti faci
# caz 4 - 18 ani - trebuie
# trebuie: 28, 38, 48, 58
# altfel nu trebuie

if varsta < 14:
    print("NU")
elif varsta == 14:
    print("DA")
elif varsta > 14 and varsta < 18:
    print("NU")
elif varsta % 10 == 8:
    print("DA")
else:
    print("NU")
