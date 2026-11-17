uczniowie = {}

n = int(input("Podaj liczbę uczniów: "))

for i in range(1, n + 1):
    imie = input("Podaj imie ucznia: ")
    m = int(input("Podaj ilość ocen: "))
    oceny = []
    for j in range(1, m + 1):
        ocena = float(input("Podaj ocene: "))
        oceny.append(ocena)
        uczniowie[imie] = oceny

najlepszy_uczen = ""
najwyzsza_srednia = -1.0

for imie, oceny in uczniowie.items():
    srednia = sum(oceny)/len(oceny)
    print(f"{imie}: średnia {srednia:.2f}")

    if srednia > najwyzsza_srednia:
        najwyzsza_srednia = srednia
        najlepszy_uczen = imie

print(f"Najlepszy: {najlepszy_uczen} ({najwyzsza_srednia:.2f})")
