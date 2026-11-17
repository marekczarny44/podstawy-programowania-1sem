ip = input("Wprowadź adres IP: ")
parts = ip.split(".")
check = 0

if len(parts) == 4:
    for i in parts:
        if not i.isdigit():
            print("NIEPRAWIDŁOWY: oktet nie jest cyfrą")
            break
        elif i == "":
            print("NIEPRAWIDŁOWY: pusty oktet")
            break
        if int(i) < 0 or int(i) > 255:
            print("NIEPRAWIDŁOWY: oktet poza zakresem 0-255")
            break
        if not str(int(i)) == i:
            print("NIEPRAWIDŁOWY: wpisane zera wiodące")
            break

        check += 1
else:
    print("NIEPRAWIDŁOWY: liczba oktetów różna od 4")

if check == 4:
    print("POPRAWNY")
