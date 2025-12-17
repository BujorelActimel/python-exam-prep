a = 12
b = 10

c = [1, 1, 1, 1, 1, 1, 2, 2, 2, 4, 4, 4] # lista
d = set(c) # set

print(c)
print(d)

studenti = ["Mihai", "Andrei", "Ioana", "Delia", "Ioana", "Ioana"]

# len - lungimea unei liste

for i in range(0, len(studenti)):
    if studenti[i] == "Ioana":
        print("da")

for st in studenti:
    if st == "Ioana":
        print("da")


studenti = {
    "Mihai": 9.83,
    "Andrei": 7.57,
    "Ioana": 8,
    "Delia": 10,
}

for nume in studenti:
    if studenti[nume] > 8:
        print(f"{nume} are bursa")
