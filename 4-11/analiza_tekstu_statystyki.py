statystyki = {
    "zdania": 0,
    "slowa": 0,
    "najdluzsze_slowo": '',
    "najczestsze_slowo": '',
    "srednia_dlugosc_slowa": ''
}
tekst = []

print("Wprowadź tekst (naciśnij Enter w pustej linii, aby zakończyć): ")
while True:
    linijka = input()
    if linijka == '':
        break
    tekst.append(linijka)

for zdanie in tekst:
    slowa = zdanie.split(' ')
    #ilosc_slow = len(slowa)
    #statystyki["slowa"] = statystyki.get("slowa", 0) + ilosc_slow
    #for litery in slowa:
    #    pass

print(slowa)