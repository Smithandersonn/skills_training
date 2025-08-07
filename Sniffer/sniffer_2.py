import socket
 
host = "192.168.0.14"
 
sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP) # considerando só o protocolo IP
 
sniffer.bind((host,0))
 
sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1) # captura o cabeçalho IP dos cabeçalhos
 
sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON) # Para Windows
 
while True:
   dados = sniffer.recvfrom(10000) # recebe o IP do pacote
   print (dados)


   sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF) # desabilita o modo promiscuo para Windows




''''
01 00 5e 7f ff fa fc f1 36 b3 1d 52 08 00 45 00 
00 3f 4e 01 40 00 40 11 3b ff c0 a8 00 0b ef ff 
ff fa a1 f9 3c f0 00 2b 27 c9 53 45 41 52 43 48 
20 42 53 44 50 2f 30 2e 31 0a 44 45 56 49 43 45 
30 0a 53 45 52 56 49 43 45 3d 31 0a 
'''


