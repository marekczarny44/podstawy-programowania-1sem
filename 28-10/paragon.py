n = int(input("Podaj liczbę pozycji: "))
nazwy = []
ceny = []

for i in range(n):
    nazwa, cena = input("> ").split()
    cena = float(cena)
    nazwy.append(nazwa)
    ceny.append(cena)

print(f"{"Produkt":<10}{"Cena":>9}")
print(19*'-')
for nazwa, cena in zip(nazwy, ceny):
    print(f"{nazwa:<10} {cena:>8.2f}")
print(f"Razem: {sum(ceny):.2f} ")