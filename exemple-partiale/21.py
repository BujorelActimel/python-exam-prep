figure_types_BN = {
    "cirlce": "rounded",
    "sphere": "rounded",
    "square": "angled",
    "triangle": "angled",
    "cube": "angled",
}

for figure_BN in figure_types_BN:
    if figure_types_BN[figure_BN] == "angled":
        print(figure_BN)
