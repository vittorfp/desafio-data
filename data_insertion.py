import time
import numpy as np
import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import json


# callback chamada quando o servidor consegue se conectar ao broker
def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Conectado ao broker")
	client.subscribe("sensors/#")


# callback chamada quando o chega alguma mensagem
def on_message(client, userdata, msg):
	global influx
	entrada = json.loads( msg.payload )
	print(entrada['valor'])
	influx.write_points( [{ "fields": {"valor": float(entrada['valor'])},  "measurement": 'temperatura' }] )

def setupMQTT():
	# Constroi um cliente MQTT
	mqttClient = mqtt.Client()

	# Define as callbacks
	mqttClient.on_connect = on_connect
	mqttClient.on_message = on_message

	# Conecta e fica rodando infinitamente
	mqttClient.connect('127.0.0.1', 1883 , 60)
	mqttClient.loop_forever()


influx = InfluxDBClient('localhost', 8086, '', '', 'telegraf')
setupMQTT()
