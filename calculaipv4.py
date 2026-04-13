ipv4 = '192.168.1.10'.split('.') #separa a string usando o ponto como divisor

ip_int = []

for i  in ipv4:
     ip_int.append(int(i)) #converte cada parte para inteiro e adiciona na lista

prefixo = 24
mask_int = []

mask_bin = ((1 << prefixo) - 1) << (32 - prefixo) # cria a máscara em binário (32 bits)
# (1 << prefixo) cria um número com 1 seguido de 'prefixo' zeros
# subtrair 1 transforma em 'prefixo' bits iguais a 1

mask_bin = mask_bin & 0xFFFFFFFF # garante que o número tenha apenas 32 bits

for i in range(4):
    shift = 24 - (i * 8)     # define o deslocamento de bits para cada octeto
    mask_int.append((mask_bin >> shift) & 255) # desloca os bits e pega apenas os últimos 8 bits (1 octeto)


rede = []
for i in range(4):
     rede.append(ip_int[i] & mask_int[i]) #operaçao bit a bit entre o ip e mask


broadcast = []
for i in range(4):
    broadcast.append(rede[i] | (~mask_int[i] & 255)) # (~mask_int[i]) inverte os bits da mask (& 255) garante que fique 8 bits validos

gateway = rede.copy() # cria o gateway como cópia do endereço de rede
gateway[3] += 1 # soma 1 no último octeto → primeiro IP válido da rede

hosts = (2 ** (32 - prefixo)) - 2 # calcula a quantidade de hosts possíveis
          
print (f'Endereço da rede: {rede}')
print (f'Endereço de broadcast: {broadcast}')
print (f'Endereço gateway: {gateway}')
print (f'Hosts que podem existir na rede: {hosts}')