import serial
import paho.mqtt.client as mqtt
from time import sleep

ser = serial.Serial("/dev/ttyS0", 115200)

mqtt_broker = "localhost"
mqtt_port = 1883
mqtt_topic = "esp32/data"
mqtt_packet = "esp32/packet"

mqtt_user = "greentech"
mqtt_password = "Greentech@01"

client = mqtt.Client()

client.username_pw_set(mqtt_user, mqtt_password)

client.connect(mqtt_broker, mqtt_port, 60)

while True:
	line = ser.readline().decode('utf-8').strip()
	if line:
		print(f"Recebido do ESP32: {line}")

	if "Mensagem do ESP32 para a Raspberry Pi" in line:
		client.publish(mqtt_topic,line)

	elif "Received packet" in line:
		client.publish(mqtt_packet,line)

	sleep(1) 