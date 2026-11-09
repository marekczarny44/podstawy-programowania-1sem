zdanie = input("Wprowadź zdanie: ")
slowa = zdanie.split(" ")

licznik = {}

for s in slowa:
    licznik[s] = licznik.get(s, 0) + 1
for k, v in licznik.items():
    print(f"{k}:{v}")