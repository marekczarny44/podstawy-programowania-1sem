biala_lista = ['192.168.1.10', '10.0.0.5', '172.16.0.1', '192.168.1.10', '10.0.0.5']

zbior = set(biala_lista)
sort = sorted(zbior)

for ip in sort:
    print(ip)