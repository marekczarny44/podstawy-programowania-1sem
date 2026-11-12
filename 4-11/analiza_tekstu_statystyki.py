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

tekst_tymczasowy = tekst.replace("?", ".").replace("!", ".")
zdania = [zdanie.strip() for zdanie in tekst_tymczasowy.split('.') if zdanie.strip()]

statystyki["ilosc_zdan"] = len(zdania)

slownik_in_slownik = statystyki["slowa_slownik"]

for zdanie in zdania:
    slowa = zdanie.split(' ')
    statystyki['ilosc_slow'] += len(slowa)
    for slowo in slowa:
        slownik_in_slownik[slowo] = slownik_in_slownik.get(slowo, 0) +1

najczestsze = max(slownik_in_slownik, key=slownik_in_slownik.get)
najdluzsze = max(slownik_in_slownik, key=len)

suma_znakow = sum(
    len(slowo) * liczba for slowo, liczba in slownik_in_slownik.items()
)
wszystkie_slowa = sum(slownik_in_slownik.values())

srednia_wazona = suma_znakow / wszystkie_slowa

print(f"Zdania: {statystyki['ilosc_zdan']}")
print(f"Slowa: {statystyki['ilosc_slow']}")
print(f"Najdluzsze slowo: {najdluzsze}")
print(f"Najczestsze slowo: {najczestsze} ({slownik_in_slownik[najczestsze]})")
print(f"Srednia dlugosc slowa: {srednia_wazona:.2f}")
