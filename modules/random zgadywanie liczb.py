import random
#random.seed(42)

cel = random.randint(1, 100)

n = 0

while True:
    proba = int(input("Podaj liczbę: "))
    if proba > cel:
        n += 1
        print("Za dużo")
    elif proba < cel:
        n += 1
        print("Za mało")
    else:
        n += 1
        print(f"Brawo! Zgadłeś w {n} próbach!")
        break