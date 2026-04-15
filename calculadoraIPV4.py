ipv4 = input('Digite um número IPv4 (quatro valores entre 0 e 255, separados por .) : ').split('.')
prefixo = int(input('Digite uma máscara de rede (um número entre 2 e 32): '))


ip_int = []
for i  in ipv4:
     ip_int.append(int(i)) 

mask_int = []
mask_bin = ((1 << prefixo) - 1) << (32 - prefixo) 

mask_bin = mask_bin & 0xFFFFFFFF 
for i in range(4):
    shift = 24 - (i * 8)     
    mask_int.append((mask_bin >> shift) & 255) 


rede = []
for i in range(4):
     rede.append(ip_int[i] & mask_int[i]) 


broadcast = []
for i in range(4):
    broadcast.append(rede[i] | (~mask_int[i] & 255)) 

gateway = rede.copy() 
gateway[3] += 1 

hosts = (2 ** (32 - prefixo)) - 2 
          
print (f'Endereço da rede: {rede}')
print (f'Endereço de broadcast: {broadcast}')
print (f'Endereço gateway: {gateway}')
print (f'Hosts que podem existir na rede: {hosts}')