import time
import numpy as np
import paho.mqtt.client as mqtt

def mqtt_publish(value,mqttc):

	mqttc.publish('sensors/temperatura', \
					payload='{ \"data\":'+str(time.time() - 10800)+', \"valor\":'+ str(value) +'}', \
					qos=0, \
					retain=False
		)


try:
	mqttc = mqtt.Client()
	mqttc.connect("127.0.0.1", 1883, 60)
	mqttc.loop_start()
except:
	print("Falha na conexao mqtt")

try:
	while True:
		value = np.random.randn()* 100
		print(value)
		mqtt_publish(value,mqttc)
		time.sleep(1)

except:
	print("Encerrando...")