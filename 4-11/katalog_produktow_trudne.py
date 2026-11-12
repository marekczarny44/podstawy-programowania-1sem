def pobierz_produkty(nazwa, kategoria, cena):
    produkty = (nazwa, kategoria, cena)

def utworz_slownik_kategorii(produkty):
    pass

def wyswietl_kategorie(slownik, kategorie):
    pass

def main():
    pass

# chuj wie czy to wszystko poniżej nie powinno być w funkcji main()
# tu (albo w mainie) powinien być tylko while, który od razu wysyła wpisane pola do funkcji pobierz_produkty() która sprawdza poprawność linijek
while True:
    linia = input("Podaj produkty: ")
    if linia.startswith("koniec"):
        break
    pola = [p.strip() for p in linia.split(",")]

    if len(pola) != 3 or not pola[2].replace(".","",1).isdigit():
        print(f"Błędny format: {linia}")
    else:
        pobierz_produkty(pola[0], pola[1], pola[2])