def kategoryzuj(cena):
    if cena < 10:
        return "tani"
    elif 10 <= cena < 50:
        return "średni"
    elif 50 <= cena < 100:
        return "drogi"
    elif cena >= 100:
        return "luksusowy"

nazwa = input("Podaj nazwę produktu: ")
cena = float(input("Podaj cenę: "))
kat = kategoryzuj(cena)
print(f"{nazwa}: {kat} ({cena} zl)")
