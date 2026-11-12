def szyfruj(tekst, klucz):
    wynik = ""
    for c in tekst:
        if c.isalpha():
            znak = chr((ord(c.upper()) - 65 + klucz) % 26 + 65)
            wynik += znak
        else:
            wynik += c
    return wynik

def odszyfruj(tekst, klucz):
    wynik = ""
    for c in tekst:
        if c.isalpha():
            znak = chr((ord(c.upper()) - 65 - klucz) % 26 + 65)
            wynik += znak
        else:
            wynik += c
    return wynik

text = input("Podaj tekst do zaszyfrowania: ")
key = int(input("Podaj klucz szyfrowania: "))

print(f"Zaszyfrowano: {szyfruj(text, key)}")
print(f"Odszyfrowano: {odszyfruj(szyfruj(text, key), key)}")