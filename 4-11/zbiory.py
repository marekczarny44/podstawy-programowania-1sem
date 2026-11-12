a = set(x.strip() for x in input("Podaj słuchaczy kursu A: ").split(','))
b = set(y.strip() for y in input("Podaj słuchaczy kursu B: ").split(','))

wspolni = sorted(a & b)
tylkoA = sorted(a - b)
rozneOsoby = sorted(a | b)

if len(wspolni) > 0:
    print("Oba kursy: ", ', '.join(wspolni))
else:
    print("Oba kursy: -")

if len(tylkoA) > 0:
    print("Tylko kurs A: ", ', '.join(tylkoA))
else:
    print("Tylko kurs A: -")

print(f"Łącznie osób: {len(rozneOsoby)}")