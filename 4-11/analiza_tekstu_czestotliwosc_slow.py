slownik = {}
tekst_tablica = []

print("Wprowadź tekst (naciśnij Enter w pustej linii, aby zakończyć): ")
while True:
    linijka = input()
    if linijka == '':
        break
    tekst_tablica.append(linijka)

tekst = " ".join(tekst_tablica)
slowa = tekst.lower().split()

for s in slowa:
    slownik[s] = slownik.get(s, 0) + 1

sortuj = sorted(slownik.items(), key=lambda x: x[1], reverse=True)[:5]

for k, v in sortuj:
    print(f"{k}: {v}")