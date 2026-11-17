tryb = input("Wybierz tryb (szyfruj, deszyfruj): ")
tekst = input("Podaj tekst do zaszyfrowania: ")
klucz = int(input("Podaj klucz szyfrowania: "))

wynik = ""

for c in tekst:
    if c.isalpha():
        if tryb.lower() == 'szyfruj':
            znak = chr((ord(c.upper()) - 65 + klucz) % 26 + 65)
        elif tryb.lower() == 'deszyfruj':
            znak = chr((ord(c.upper()) - 65 - klucz) % 26 + 65)
        else:
            print("Zły tryb")
            break
        wynik += znak
    else:
        wynik += c

print(wynik)