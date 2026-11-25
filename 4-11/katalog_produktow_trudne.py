def pobierz_produkty():
    produkty = []
    while True:
        linia = input("Podaj produkty: ").lower()
        if linia.strip().startswith("koniec"):
            break

        pola = [p.strip() for p in linia.split(",")]

        if len(pola) != 3 or not pola[2].replace(".", "", 1).isdigit():
            print(f"Błędny format: {linia}")
            continue
        else:
            nazwa = pola[0]
            kategoria = pola[1]
            cena = pola[2]
            produkty.append(tuple(nazwa, kategoria, cena)) #naprawić to, krotka powinna być dodawana do tablicy
    return produkty

def utworz_slownik_kategorii(produkty):
    slownik = {}
    for nazwa, kategoria, cena in produkty:
        if kategoria not in slownik:
            slownik[kategoria] = []
    #słownik ma mapować kategoria->lista nazw produktów, więc do listy dodać samą nazwę (bez ceny)
    return slownik

def wyswietl_kategorie(slownik, kategoria):
    if kategoria in slownik:
        "".join(slownik[kategoria])
        print(f"Produkty w kategorii {kategoria}: {polaczone_nazwy}") # do zrobienia polaczone_nazwy
    else:
        print("Brak produktów w kategorii")

def main():
    produkty = pobierz_produkty()
    print(f"Wczytano produktów: {len(produkty)}")
    slownik = utworz_slownik_kategorii(produkty)
    szukana_kategoria = input("Podaj nazwę kategorii: ").strip()
    wyswietl_kategorie(slownik, szukana_kategoria)

if __name__ == '__main__':
    main()