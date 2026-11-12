haslo = input("Podaj hasło: ")

ma_wielka = False
ma_mala = False
ma_cyfre = False
ma_znak = False

for letter in haslo:
    if letter.isupper():
        ma_wielka = True
    if letter.islower():
        ma_mala = True
    if letter.isdigit():
        ma_cyfre = True
    if letter in "!@#$%^&*":
        ma_znak = True

ma_dlugosc = len(haslo) >= 8

print(f"{'[OK] Dlugosc >= 8' if ma_dlugosc else '[BŁĄD] Zbyt krotkie haslo'}")
print(f"{'[OK] Wielka litera' if ma_wielka else '[BŁĄD] Brak wielkiej litery'}")
print(f"{'[OK] Mala litera' if ma_mala else '[BŁĄD] Brak malej litery'}")
print(f"{'[OK] Cyfra' if ma_cyfre else '[BŁĄD] Brak cyfry'}")
print(f"{'[OK] Znak specjalny' if ma_znak else '[BŁĄD] Brak znaku specjalnego'}")

if ma_dlugosc and ma_znak and ma_mala and ma_cyfre and ma_wielka:
    print("Hasło silne!")
else:
    print("Hasło słabe!")

