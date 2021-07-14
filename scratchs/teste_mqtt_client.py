# Cliente assinante (subscriber)
import paho.mqtt.client as mqtt

Broker = "test.mosquitto.org"
TopicoSubscribe = "aluiziorocha/atuador1"
PortaBroker = 1883
KeepAliveBroker = 60

def on_connect(client, userdata, flags, rc):
    print("[Connection status] " + str(rc))
    client.subscribe(TopicoSubscribe)
def on_message(client, userdata, msg):
    print("[Topic/MSG] "+msg.topic+ " / "+ str(msg.payload))

print("[STATUS] Inicializando MQTT...")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(Broker, PortaBroker, KeepAliveBroker)
client.loop_forever()