ipv4 = '192.168.1.10'.split('.') #separa a string nos pontos

ip_int = []

for i  in ipv4:
     ip_int.append(int(i)) #converte para inteiro

prefixo = 24
mask_int = []
mask_bin = 0xFFFFFFFF #começa com 32 bits em 1
mask_bin = mask_bin << (32 - prefixo) #cria os bits de host (os zeros)
mask_bin = mask_bin & 0xFFFFFFFF #garante 32 bits

for i in range(4):
    shift = 24 - (i * 8)
    mask_int.append((mask_bin >> shift) & 255)


rede = []
for i in range(4):
     rede.append(ip_int[i] & mask_int[i]) #operaçao bit a bit entre o ip e mask


broadcast = []
for i in range(4):
    broadcast.append(rede[i] | (~mask_int[i] & 255)) # (~mask_int[i]) inverte os bits da mask (& 255) garante que fique 8 bits validos
          
          
print (ip_int)
print (mask_int)
print (rede)
print (broadcast)