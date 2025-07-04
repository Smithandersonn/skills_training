import datetime
import socket

 #127.0.0.1 é o endereço IPv4 para "localhost" (a própria máquina).
 #A porta 8800 é arbitrária (pode ser qualquer número entre 1024 e 65535, desde que não esteja em uso).

host = '127.0.0.1'                                              # o mesmo que localhost
porta = 8800                                                    # porta da conexão

"""
socket.socket(): Cria um novo objeto socket (ponto de comunicação).
socket.AF_INET: Define que o socket usará IPv4 (endereços no formato x.x.x.x).
socket.SOCK_STREAM: Indica que o socket usará TCP (Transmission Control Protocol), que é orientado à conexão e confiável.
"""

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #estou usando TCP/IP
recebe = (host, porta)
soquete.bind(recebe)                                            #soquete.bind(): Associa o socket ao endereço e porta especificados.
soquete.listen(2)                                               #soquete.listen(2): Coloca o socket em modo de escuta para aceitar conexões.
#O argumento 2 define o backlog, ou seja, o número máximo de conexões pendentes na fila antes de recusar novas

"""
datetime.now().strftime('%d/%m/%Y - %H:%M:%S' - formatarmos a data e a hora do sistema:
    porque a data vem no padrão britânico: ano/mês/dia e os segundos são mostrados em frações de até bilissegundos.
        soquete.accept(): Método que bloqueia a execução até que um cliente se conecte.
            Retorna dois valores:
            conexao: Um novo objeto socket para comunicação com o cliente específico.
                enderecoIP: Uma tupla contendo (IP do cliente, porta do cliente).
"""

print('\nSERVIDOR INICIADO...IP: ', host, 'PORTA: ', porta,' EM: ',datetime.datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))

while True:                                                     #Cria um loop infinito para que o servidor fique continuamente aceitando novas conexões.
    conexao, enderecoIP = soquete.accept()
    print('\nSERVIDOR ACESSADO PELO CLIENTE:', enderecoIP, 'EM: ',datetime.datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))

    while True:                                                 #mantém o servidor continuamente verificando por novas mensagens.
        mensagem = conexao.recv(2048)                           #tenta receber até 2048 bytes de dados do cliente. O número 2048 é o tamanho do buffer.
        if not mensagem:                                        # Se mensagem estiver vazia (sem dados), significa que o cliente fechou a conexão, então o loop é interrompido com break
            break
        print('\nIP CLIENTE:', enderecoIP)                      #Mostra o endereço IP do cliente
        print('MENSAGEN RECEBIDA: ', mensagem.decode(),' - ',datetime.datetime.now().strftime('%H:%M:%S'))  #mensagem.decode()) Decodifica os bytes recebidos para string usando .decode() e exibe a mensagem

    print('CONEXÃO COM O CLIENTE FINALIZADA...', enderecoIP, ' EM: ',datetime.datetime.now().strftime('%d/%m/%Y - %H:%M:%S')) #Informa que a conexão com o cliente foi finalizada
    conexao.close()                                             #Fecha o socket de conexão com conexao.close()