import sys

if len(sys.argv) < 4:
    print("Użycie: python3 kalkulator_sys_argv.py liczba1 liczba2 operacja")
    sys.exit()

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    op = sys.argv[3]

    match op:
        case "dodaj":
            print(f"{a} dodaj {b} = {a+b}")
        case "odejmij":
            print(f"{a} odejmij {b} = {a-b}")
        case "pomnoz":
            print(f"{a} pomnoz {b} = {a*b}")
        case "podziel":
            print(f"{a} podziel {b} = {a/b}")
        case _:
            print(f"Nieznana operacja: {op}")
except ValueError:
    print("Błąd: wpisz poprawną liczbę")
except ZeroDivisionError:
    print("Błąd: dzielenie przez zero")