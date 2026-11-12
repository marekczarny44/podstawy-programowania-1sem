wiersze = int(input("Podaj liczbę wierszy: "))
kolumny = int(input("Podaj liczbę kolumn: "))

macierz = [[int(x) for x in input().split()] for _ in range(wiersze)]

print("Macierz:")
for j in range(wiersze):
    print(" ".join(str(macierz[j][i]) for i in range(kolumny)))

print("Transpozycja:")
for j in range(kolumny):
    print(" ".join(str(macierz[i][j]) for i in range(wiersze)))