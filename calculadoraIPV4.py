ipv4 = '192.168.1.10'.split('.')

ip_int = []

for i in ipv4:
     ip_int.append(int(i))

prefixo = 24
mask_int = []

for i in range(4):
    if prefixo >= 8:
        mask_int.append(255)
        prefixo -= 8
    elif prefixo > 0:
        mask_int.append(256 - (2 ** (8 - prefixo)))
        prefixo = 0
    else:
        mask_int.append(0)

        

rede = []
for i in range(4):
     rede.append(ip_int[i] & mask_int[i])