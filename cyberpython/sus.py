sus = ['cryptominer','keylogger','backdoor','rootkit']

n = int(input("Podaj ilość linii: "))
wejscie = []

for i in range(n):
    linia = input("Wprowadź linię w formacie (PID NAZWA CPU% MEM%): ")
    wejscie.append(linia)

f = open('alert_procesy.txt', 'w')


for proces in wejscie:
    parts = proces.split()
    cpu = parts[2]
    mem = parts[3]
    if float(cpu) > 80:
        pass
    if float(mem) > 50:
        pass



f.close()
