octal = input("Podaj kod uprawnień: ")

if len(octal) != 3 or not all(znak in "01234567" for znak in octal):
    print("Zły kod")
else:
    uprawnienia = []

    for znak in octal:
        cyfra = int(znak)
        tekst = ""
        tekst += 'r' if cyfra & 4 else '-'
        tekst += 'w' if cyfra & 2 else '-'
        tekst += 'x' if cyfra & 1 else '-'
        uprawnienia.append(tekst)

    wlasciciel, grupa, inni = uprawnienia

    print("Właściciel:", wlasciciel)
    print("Grupa:     ", grupa)
    print("Inni:      ", inni)
    print("Pełne:     ", "".join(uprawnienia))