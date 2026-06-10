import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('httpbin.org', 80))

my_sock.send (b"GET /image/png HTTP/1.1\r\n"+
              b"Host: httpbin.org\r\n"+
              b"\r\n")

data = my_sock.recv(4096)
pos2NL = data.find(b"\r\n\r\n")
headers = data[:pos2NL].split(b'\r\n')

is_chunked = False #assume inicialmente q a resposta nao usa chunked

len_data = -1
for header in headers[1:]:
    header = header.split(b":") #separa nome e valor do cabeçalho
    if header[0] == b"Content-Length": #procura tamanho total dos dados caso exista
        len_data = int(header[1])
    if header[0] == b"Transfer-Encoding" and header[1] == b" chunked": #verifica se o servidor ta enviando os dados em chunks
        is_chunked = True

if len_data != -1:
    print (f"Content-Length={len_data}")
    data = data[pos2NL+4:]
    while len(data) < len_data:
        data += my_sock.recv(4096)

    fd = open("porco.png", "wb")
    fd.write(data)
    fd.close()

elif is_chunked: 
    data = data[pos2NL+4:] #remove os cabeçalhos e mantem apenas os dados da resposta
    pos = data.find(b"\r\n") #localiza o tamanho do primeiro chunked
    chunk_size = int(data[:pos], 16) #converte o tamanho do chunk de hexa para decimal
    result = b"" #armazena os dados recebidos ja reconstruidos
    while chunk_size != 0: #continua lendo os chunks ate encontrar marcador fim
        data = data[pos+2:] #remove a linha q contem o tamanho do chunk
        while len(data) < chunk_size + 2: #garante q todo o chunk foi recebido
            data += my_sock.recv(4096)
        result += data[:chunk_size] #adiciona o conteudo do chunk ao resultado final
        data = data[chunk_size+2:] #remove o chunk ja processado da variavel de trabalho
        pos = data.find(b"\r\n") # procura o tamanho do proximo chunck
        chunk_size = int(data[:pos], 16) # converte o proximo tamanho para decimal
    fd = open("porco.png", "wb")
    fd.write(result)
    fd.close()
else:
    print ("Content-Length não encontrado!")
    my_sock.close()
