import time
import socket
import sys
import numpy as np

port = 8094
host = '127.0.0.1'
host = '127.0.0.1'
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()


while True:
	value1 = 400 + np.absolute(np.random.randn()* 150)
	value2 = np.absolute(np.random.randn()* 150)
	msg = '{ \"valor1\":'+ str(value1) +',\"valor2\":'+ str(value2) +' }'
	print('Enviando: ' + str(msg) )
	s.sendto(str(msg) , (host,port	) )
	time.sleep(2)

try:
	pass
except:
	print("Encerrando...")
	exit(1)