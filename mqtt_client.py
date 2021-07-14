import paho.mqtt.client as mqtt


class MQTTClient:
    def __init__(self, broker: str, topic: str, port: int, keepalive: int) -> None:
        """Receive a broker string, a topic, port number, and keepalive time and set as attributes"""
        self.client = mqtt.Client()
        self.broker = broker
        self.topic = topic
        self.port = port
        self.keepalive = keepalive
        
    def connect_broker(self, broker: str = None, port: int = None, keepalive: int = None):
        if broker:
            self.broker = broker
        if port:
            self.port = port
        if keepalive:
            self.keepalive = keepalive
        self.client.connect(self.broker, self.port, self.keepalive)

    def subscribe(self, topic: str = None):
        if topic:
            self.topic = topic
        self.client.subscribe(self.topic)

    def set_on_connect_callback(self, func):
        self.client.on_connect = func

    def set_on_message_callback(self, func):
        self.client.on_message = func

    def lets_go(self):
        self.client.loop_forever()
