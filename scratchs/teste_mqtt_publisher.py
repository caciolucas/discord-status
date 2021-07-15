# Cliente publicante (publisher)
import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt

load_dotenv()

Broker = "test.mosquitto.org"
PortaBroker = 1883
KeepAliveBroker = 60
TopicoSubscribe = os.getenv('MQTT_TOPIC')
print("[STATUS] Inicializando MQTT...")
client = mqtt.Client()
client.connect(Broker, PortaBroker, KeepAliveBroker)
mensagem = ""
while mensagem != "sair":
    mensagem = input("Mensagem a publicar? [sair –encerra]: ")
    if mensagem != "sair":
        client.publish(TopicoSubscribe, mensagem, 0, False)
client.disconnect()