imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
wiek = int(input("Podaj wiek: "))

osoba = {'imie':imie,'nazwisko':nazwisko,'wiek':wiek}

for klucz, wartosc in osoba.items():
    print(f"{klucz}: {wartosc}")