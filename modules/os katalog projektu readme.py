import os

nazwa = input("Podaj nazwę katalogu: ")

os.makedirs(nazwa, exist_ok=True)

sciezka = os.path.join(nazwa, "README.txt")
with open(sciezka, "w", encoding='utf-8') as f:
    f.write("Hello world!")

print(f"Utworzono katalog: {nazwa}")
print(f"Plik README.txt istnieje: {os.path.exists(sciezka)}")
print(f"Zawartość katalogu: {os.listdir(nazwa)}")
