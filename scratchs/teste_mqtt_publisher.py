# Cliente publicante (publisher)
import paho.mqtt.client as mqtt

Broker = "test.mosquitto.org"
PortaBroker = 1883
KeepAliveBroker = 60
TopicoSubscribe = "aluiziorocha/atuador1"
print("[STATUS] Inicializando MQTT...")
client = mqtt.Client()
client.connect(Broker, PortaBroker, KeepAliveBroker)
mensagem = ""
while mensagem != "sair":
    mensagem = input("Mensagem a publicar? [sair –encerra]: ")
    if mensagem != "sair":
        client.publish(TopicoSubscribe, mensagem, 0, True)
client.disconnect()