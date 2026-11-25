def ustaw_wiek(tekst):
    wiek = int(tekst)
    if wiek < 0 or wiek > 150:
        raise ValueError("Wiek poza zakresem 0-150")
    else:
        return f"Zapisano wiek: {wiek}"

tekst = input("Wprowadź wiek: ")
try:
    print(ustaw_wiek(tekst))

except ValueError as e:
    print(f"Błąd: {e}")

finally:
    print("Koniec walidacji")
