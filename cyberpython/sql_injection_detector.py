'''
Napisz program, który sprawdzi, czy tekst podany przez użytkownika zawiera podejrzane wzorce SQL Injection.

Podejrzane wzorce (case-insensitive):
- ' OR 1=1
- ' OR ''='
- '; DROP TABLE
- ' UNION SELECT
- '--  (komentarz SQL)

Jeśli wykryto podejrzany wzorzec, wypisz '[ALERT] Wykryto potencjalny SQL Injection!' i nazwy wykrytych wzorców.
Jeśli nie: '[OK] Brak podejrzanych wzorców'
'''

wzorzec = ["OR 1=1", "OR ''=", "; DROP TABLE", "UNION SELECT", "--"]

tekst = input("Podaj tekst: ")
wykryte_wzorce = []
wykryte = ''
flaga = False

for przypadek in wzorzec:
    if przypadek.lower() in tekst.lower():
        wykryte_wzorce.append(przypadek)
        flaga = True

if flaga:
    wykryte = ', '.join([p for p in wykryte_wzorce])
    print("[ALERT] Wykryto potencjalny SQL Injection")
    print(f"Wykryte wzorce: {wykryte}")
else:
    print("[OK] Brak podejrzanych wzorców")
