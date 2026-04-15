import hashlib

entrada = input('Digite a mensagem para gerar o hash: ')
entrada_bytes = entrada.encode('utf-8')
bits_zero = int(input('Digite quantos bits zero o hash deve ter no início: '))

for x in range (0, 1000000):
    nonce_bytes = x.to_bytes(4, 'big')
    dados = nonce_bytes + entrada_bytes
    h = hashlib.sha256(dados).digest()
    h_int = int.from_bytes(h, 'big')
    bits_zero_str = bin(h_int)[2:].zfill(256)

    if bits_zero_str.startswith("0" * bits_zero):
        print('O nonce é:', x)
        break
else:
    print('NONCE NÃO ENCONTRADO!')