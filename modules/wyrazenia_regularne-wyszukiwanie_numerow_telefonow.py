import re

tekst = input("Wprowadź tekst: ")

numery = re.findall(r'\d{3}[- ]?\d{3}[- ]?\d{3}', tekst)

print(f"Znaleziono: {len(numery)}")

for n in numery:
    c = re.sub(r'\D','', n)
    print(c[:3] + '-' + c[3:6] + '-' + c[6:])