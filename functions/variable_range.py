licznik = 0

def zarejestruj(imie):
    global licznik
    licznik += 1
    return f"Zarejestrowano {imie} (nr {licznik})"

def test_lokalny():
    licznik = 100
    print(f"Lokalnie: {licznik}")

n = int(input("Podaj liczbę imion do wpisania: "))

for i in range(n):
    name = input("Podaj imię: ")
    print(zarejestruj(name))

test_lokalny()
print(f"Globalnie: {licznik}")