import time
import numpy as np
import paho.mqtt.client as mqtt

def mqtt_publish(value,mqttc):

	mqttc.publish('sensors/temperatura', \
					payload='{ \"valor\":'+ str(value) +'}', \
					qos=0, \
					retain=False
		)


try:
	mqttc = mqtt.Client()
	mqttc.connect("127.0.0.1", 1883, 60)
	mqttc.loop_start()
except:
	print("Falha na conexao mqtt")
	exit(1)

try:
	while True:
		value = np.absolute(np.random.randn()* 150)
		print('Enviando: ' + str(value) )
		mqtt_publish(value,mqttc)
		time.sleep(2)

except:
	print("Encerrando...")
	exit(1)