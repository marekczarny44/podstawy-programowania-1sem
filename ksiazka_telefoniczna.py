kontakty = {}

while True:
    cmd = input("Wprowadź komendę: ")
    if cmd.startswith("dodaj"):
        imie = input("Podaj imię: ")
        numer = int(input("Podaj numer: "))
        kontakty[imie] = numer
        print(f"Dodano: {imie} - {numer}")
    if cmd.startswith("szukaj"):
        imie = input("Podaj imie: ")
        if imie in kontakty:
            print(f"{imie} - {kontakty[imie]}")
        else:
            print("Nie znaleziono")
    if cmd.startswith("lista"):
        sorted(kontakty.items())
        for imie, numer in kontakty.items():
            print(f"{imie} - {numer}")
    if cmd.startswith("koniec"):
        print("Koniec")
        break