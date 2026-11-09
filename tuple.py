n = int(input("Podaj liczbę: "))
lista = []

for i in range(1,n+1):
    liczba = int(input("Wprowadź liczbę: "))
    lista.append(liczba)
krotka = tuple(lista)

print(f"Elementów: {len(krotka)}")
print(f"Min: {min(krotka)}")
print(f"Max: {max(krotka)}")
print(f"Suma: {sum(krotka)}")