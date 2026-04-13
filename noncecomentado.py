import hashlib


entrada_bytes = 'travessia'.encode('utf-8') #pega a string "travessia" e transforma em bytes

bits_zero = 5 #define com quantos bits em zero o hash começa

for x in range (0, 100000): #loop que testa vários valores de nonce
    nonce_bytes = x.to_bytes(4, 'big') #transforma o número x em 4 bytes em ordem big endian
    dados = nonce_bytes + entrada_bytes
    h = hashlib.sha256(dados).digest()#calcula o hash SHA-256
    h_int = int.from_bytes(h, 'big') #transforma o hash (bytes) em número inteiro
    bits_zero_str = bin(h_int)[2:].zfill(256) #'bin(h_int)' = converte p/ binario. '[2:] = remove 0b. '.zfill(256) = garante que tenha 256 bits

    if bits_zero_str.startswith("0" * bits_zero): #verifica se o hash começa com zeros
     print('O nonce é:', x)
     break


'''

tenta nonce
↓
gera hash
↓
verifica se começa com zeros
↓
se sim → para

'''