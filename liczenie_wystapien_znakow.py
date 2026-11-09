tekst = input("Wprowadź tekst: ").lower()
licznik = {}

for i in tekst:
    if i == " ":
        pass
    else:
        licznik[i] = licznik.get(i, 0) + 1

for k,v in sorted(licznik.items()):
    print(f"{k}:{v}")