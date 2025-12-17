# dictionar cu firme si cheltuielile firmei luna
# dictionare cu firme si cifra de afaceri
# afiseze profitul fiecarei 

cheltuieli = {
    "TechSolutions": [25000, 18000, 22000, 15000, 30000],
    "BuildCo": [45000, 52000, 38000, 41000],
    "MarketPro": [8000, 12000, 9500, 11000, 7500],
    "GreenEnergy": [60000, 55000, 48000, 62000, 58000],
    "FoodExpress": [22000, 19000, 24000, 21000, 18000, 20000]
}

income = {
    "TechSolutions": 145000,
    "BuildCo": 180000,
    "MarketPro": 65000,
    "GreenEnergy": 275000,
    "FoodExpress": 135000
}

# iau fiecare firma
# pentru firma curenta iau incomeul
# din income scad toate cheltuielile
# afisez profit daca este profitabil
# in caz contrar afisez 

for firma in cheltuieli:
    profit = income[firma]
    for cheltuiala in cheltuieli[firma]:
        profit = profit - cheltuiala
    if profit > 0:
        print("Firma", firma, "are profit", profit)
    else:
        print(f"Firma {firma} nu este profitabila")
