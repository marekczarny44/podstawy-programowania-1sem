line1 = input("Pierwsza linia tekstu: ")
line2 = input("Druga linia tekstu: ")
line3 = input("Trzecia linia tekstu: ")

with open('notatki.txt', 'w') as f:
    f.write(line1 + '\n')
    f.write(line2 + '\n')
    f.write(line3 + '\n')

with open('notatki.txt', 'r') as f:
    print(f.read())