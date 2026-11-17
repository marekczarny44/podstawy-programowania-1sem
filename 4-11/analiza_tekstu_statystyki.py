statystyki = {
    "ilosc_zdan": 0,
    "ilosc_slow": 0,
    "slowa_slownik": {}
}
tekst_tablica = []

print("Wprowadź tekst (naciśnij Enter w pustej linii, aby zakończyć): ")
while True:
    linijka = input()
    if linijka == '':
        break
    tekst_tablica.append(linijka)

tekst = " ".join(tekst_tablica)

if tekst == "":
    print("Brak wpisanego tekstu")
else:
    tekst_tymczasowy = tekst.replace("?", ".").replace("!", ".")
    zdania = [zdanie.strip() for zdanie in tekst_tymczasowy.split('.') if zdanie.strip()]

    statystyki["ilosc_zdan"] = len(zdania)

    slownik_in_slownik = statystyki["slowa_slownik"]

    for zdanie in zdania:
        slowa = zdanie.split()
        statystyki['ilosc_slow'] += len(slowa)
        for slowo in slowa:
            nowe_slowo = "".join(znak for znak in slowo if znak.isalnum()).lower()
            slownik_in_slownik[nowe_slowo] = slownik_in_slownik.get(nowe_slowo, 0) +1

    max_czestotliwosc = max(slownik_in_slownik.values())
    najczestsze = [s for s, ilosc in slownik_in_slownik.items() if ilosc == max_czestotliwosc]

    max_dlugosc = len(max(slownik_in_slownik, key=len))
    najdluzsze = [c for c in slownik_in_slownik if len(c) == max_dlugosc]

    suma_znakow = sum(
        len(slowo) * liczba for slowo, liczba in slownik_in_slownik.items()
    )
    wszystkie_slowa = sum(slownik_in_slownik.values())

    srednia_wazona = suma_znakow / wszystkie_slowa

    print(f"Zdania: {statystyki['ilosc_zdan']}")
    print(f"Slowa: {statystyki['ilosc_slow']}")
    if len(najdluzsze) > 1:
        print("Najdluzsze slowo (remis):")
        for l in najdluzsze:
            print("\t",l)
    else:
        for el in najdluzsze:
            print(f"Najdluzsze slowo: {el}")
    if len(najczestsze) > 1:
        print("Najczestsze slowo (remis):")
        for k in najczestsze:
            print(f"\t{k}: {slownik_in_slownik[k]}")
    else:
        print(f"Najczestsze slowo: {najczestsze} ({max_czestotliwosc}")
    print(f"Srednia dlugosc slowa: {srednia_wazona:.2f}")

