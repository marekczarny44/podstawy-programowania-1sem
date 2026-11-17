logi = ['10.0.0.1', '192.168.1.5', '10.0.0.1', '10.0.0.1', '192.168.1.5', '172.16.0.3', '10.0.0.1', '192.168.1.5', '172.16.0.3']

dict = {}

for ip in logi:
    dict[ip] = dict.get(ip, 0) + 1

top_3 = sorted(dict.items(), key=lambda item: item[1], reverse=True)[:3]

for ip in top_3:
    print(f"{ip[0]}: {ip[1]} prób")