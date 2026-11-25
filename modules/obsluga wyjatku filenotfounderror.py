nazwa = input("Podaj nazwę pliku: ")

try:
    with open(nazwa, "r") as f:
        print(f.read())
except FileNotFoundError:
    print(f"Plik nie istnieje: {nazwa}")
    with open(nazwa, 'w') as f:
        pass
    print(f"Utworzono plik: {nazwa}")