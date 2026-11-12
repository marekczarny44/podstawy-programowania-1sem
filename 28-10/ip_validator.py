ip = input("Wprowadź adres IP: ")
parts = ip.split(".")
check = 0

if len(parts) == 4:
    for i in parts:
        if not i.isdigit():
            break
        elif i == "":
            break
        if int(i) < 0 or int(i) > 255:
            break
        if len(i) > 1 and i[0] == '0':
            break

        check += 1

if check == 4:
    print("Adres poprawny")
else:
    print("Adres niepoprawny")